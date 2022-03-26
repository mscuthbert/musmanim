import math

import manim as m
# noinspection PyProtectedMember
from manim.utils.rate_functions import ease_in_out_sine


class Bounce(m.Animation):
    def __init__(self,
                 m_object,
                 bound=0,
                 elasticity=0.8,
                 initial_velocity=0.0,
                 acceleration=-5,
                 above_edge=m.UP,
                 run_time=2.0,
                 lag_ratio=0.3,
                 **kwargs):
        super().__init__(m_object,
                         introducer=True,
                         run_time=run_time,
                         lag_ratio=lag_ratio,
                         **kwargs)
        self.initial_velocity = initial_velocity
        self.velocities = []
        self.last_alphas = []
        self.acceleration = acceleration
        self.elasticity = elasticity
        self.bound = bound
        self.above_edge = above_edge


    def begin(self):
        super().begin()
        for m_obj in self.get_all_mobjects():
            m_obj.to_edge(m.UP, buff=0).shift(self.above_edge)

    def interpolate_mobject(self, alpha: float) -> None:
        families = list(self.get_all_families_zipped())
        for i, mobs in enumerate(families):
            sub_alpha = self.get_sub_alpha(alpha, i, len(families))
            self.bounce_interpolate_submobject(mobs[0], mobs[1], sub_alpha, i)

    # noinspection PyUnusedLocal
    def bounce_interpolate_submobject(
        self,
        submobject: m.Mobject,
        starting_submobject: m.Mobject,
        alpha: float,
        i: int,
    ) -> m.Animation:
        if alpha == 0.0:
            self.velocities.append(self.initial_velocity)
            self.last_alphas.append(0.0)
            return self

        if alpha == 1.0:
            submobject.set_y(self.bound)
            return self

        last_alpha = self.last_alphas[i]
        self.velocities[i] += self.acceleration * (alpha - last_alpha)
        new_v = self.velocities[i]
        current_y = submobject.get_y()
        new_y = max(current_y + new_v, self.bound)
        submobject.set_y(new_y)
        if new_y == self.bound:
            new_velocity = -1 * new_v * self.elasticity
            self.velocities[i] = new_velocity
        self.last_alphas[i] = alpha
        return self


class ExcitedBase(m.Animation):
    def __init__(self, *args, num_reps=4, distance=0.15, drift=0.0, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_reps = num_reps
        self.distance = distance
        self.drift = drift

    def alpha_to_shift_amount(self, alpha):
        if alpha == 1:
            return 0
        first_quadrant = 1 / (self.num_reps*4)
        last_quadrant = 1 - first_quadrant

        # first and last quadrants need to start / end slow.
        if alpha < first_quadrant:
            return ease_in_out_sine(alpha/first_quadrant)
        if alpha > last_quadrant:
            last_quadrant_progress = (alpha-last_quadrant) / first_quadrant
            return ease_in_out_sine(last_quadrant_progress) - 1

        return math.sin(self.num_reps * m.PI * 2 * alpha)


class Agitate(ExcitedBase):
    def interpolate_submobject(
        self,
        submobject: m.Mobject,
        starting_submobject: m.Mobject,
        alpha: float,
    ) -> m.Animation:
        shift_dist = self.alpha_to_shift_amount(alpha)
        submobject.set_y(shift_dist * self.distance
                         + self.starting_mobject.get_y()
                         + self.drift * alpha)
        return self


class Confused(ExcitedBase):
    def interpolate_submobject(
        self,
        submobject: m.Mobject,
        starting_submobject: m.Mobject,
        alpha: float,
    ) -> m.Animation:
        # doubly smooth.
        shift_dist = self.alpha_to_shift_amount(self.rate_func(alpha))
        submobject.set_x(shift_dist * self.distance
                         + self.starting_mobject.get_x()
                         + self.drift * alpha
                         )
        return self
