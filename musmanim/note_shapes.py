import manim as m
import numpy as np


class Maxima(m.Polygon):
    def __init__(self, **kwargs):
        super().__init__(
            [-0.8,  0.5, 0],
            [ 0.8,  0.5, 0],
            [ 0.8, -1.5, 0],
            [ 0.7, -1.5, 0],
            [ 0.7, -0.5, 0],
            [-0.8, -0.5, 0],

            color=kwargs.get('color', m.PURPLE_C),
            fill_color=kwargs.get('fill_color', m.PURPLE_C),
            fill_opacity=kwargs.get('fill_opacity', 0.9),
            **kwargs)
        self.corner_radius = 0.05
        self.round_corners(self.corner_radius)

    def get_critical_point(self, direction):
        if np.array_equal(direction, [0, 0, 0]):
            return [0, 0, 0]
        return super().get_critical_point(direction)


class Longa(m.Polygon):
    def __init__(self, rounded=True, color=m.PURPLE_C, fill_color=None, fill_opacity=0.9, **kwargs):
        if fill_color is None:
            fill_color = color
        super().__init__(
            [-0.5, 1.5, 0],
            [ 0.5, 1.5, 0],
            [ 0.5, -0.5, 0],
            [ 0.4, -0.5, 0],
            [ 0.4, 0.5, 0],
            [-0.5, 0.5, 0],
            color=color,
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            **kwargs)
        self.shift(m.DOWN)
        if rounded:
            self.corner_radius = 0.05
            self.round_corners(self.corner_radius)
        else:
            self.corner_radius = 0.0
        self.shift(self.get_center())

    def get_critical_point(self, direction):
        if np.array_equal(direction, [0, 0, 0]):
            return np.array((0.0, 0.0, 0.0))
        return super().get_critical_point(direction)


class Breve(m.Square):
    def __init__(self,
                 color=m.PURPLE_C,
                 fill_color=None,
                 fill_opacity=0.9,
                 side_length=1.0,
                 **kwargs):
        if fill_color is None:
            fill_color = color
        super().__init__(side_length=side_length,
                         color=color,
                         fill_color=fill_color,
                         fill_opacity=fill_opacity,
                         **kwargs)
        self.corner_radius = side_length * 0.05
        self.round_corners(self.corner_radius)


class Semibreve(Breve):
    def __init__(self, side_length=0.707, **kwargs):
        super().__init__(side_length=side_length, **kwargs)
        self.rotate(m.PI / 4)


class Minim(m.Polygon):
    def __init__(self, **kwargs):
        super().__init__(
            [-0.5,  0.0, 0],
            [-0.05, 0.5, 0],
            [-0.05, 1.5, 0],
            [ 0.05, 1.5, 0],
            [ 0.05, 0.5, 0],
            [ 0.5,  0.0, 0],
            [ 0.0, -0.5, 0],
            color=kwargs.get('color', m.PURPLE_C),
            fill_color=kwargs.get('fill_color', m.PURPLE_C),
            fill_opacity=kwargs.get('fill_opacity', 0.9),
            **kwargs)
        self.corner_radius = 0.05
        self.round_corners(self.corner_radius)
        self.shift(self.get_center())

    def get_critical_point(self, direction):
        if np.array_equal(direction, [0, 0, 0]):
            return np.array((0.0, 0.0, 0.0))
        return super().get_critical_point(direction)
