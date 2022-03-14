from manim import *

MAXIMA = ''
LONGA = ''
BREVE = ''
SEMIBREVE = ''
MINIM = ''


_THEIR_TEXT = Text


class Text(_THEIR_TEXT):
    def __init__(self, t, font='Adobe Garamond Pro', color=WHITE, **kwargs):
        super().__init__(t, font=font, color=color, **kwargs)


class Bravura(Text):
    def __init__(self, t='', font_size=144, color=PURPLE_C, **kwargs):
        super().__init__(t,
                         font_size=font_size,
                         color=color,
                         font='Bravura Text',
                         **kwargs)


class Maxima(Polygon):
    def __init__(self, **kwargs):
        super().__init__(
            [-1.0,  0.5, 0],
            [ 1.0,  0.5, 0],
            [ 1.0, -1.5, 0],
            [ 0.9, -1.5, 0],
            [ 0.9, -0.5, 0],
            [-1.0, -0.5, 0],

            color=kwargs.get('color', PURPLE_C),
            fill_color=kwargs.get('fill_color', PURPLE_C),
            fill_opacity=kwargs.get('fill_opacity', 0.9),
            **kwargs)
        self.corner_radius = 0.05
        self.round_corners(self.corner_radius)

    def get_critical_point(self, direction):
        if np.array_equal(direction, [0, 0, 0]):
            return [0, 0, 0]
        return super().get_critical_point(direction)


class Longa(Polygon):
    def __init__(self, **kwargs):
        super().__init__(
            [-0.5, 1.5, 0],
            [ 0.5, 1.5, 0],
            [ 0.5, -0.5, 0],
            [ 0.4, -0.5, 0],
            [ 0.4, 0.5, 0],
            [-0.5,

             0.5, 0],
            color=kwargs.get('color', PURPLE_C),
            fill_color=kwargs.get('fill_color', PURPLE_C),
            fill_opacity=kwargs.get('fill_opacity', 0.9),
            **kwargs)
        self.shift(DOWN)
        self.corner_radius = 0.05
        self.round_corners(self.corner_radius)
        self.shift(self.get_center())

    def get_critical_point(self, direction):
        if np.array_equal(direction, [0, 0, 0]):
            return [0, 0, 0]
        return super().get_critical_point(direction)


class Breve(Square):
    def __init__(self, **kwargs):
        side_length = kwargs.get('side_length', 1)
        super().__init__(color=kwargs.get('color', PURPLE_C),
                         fill_color=kwargs.get('fill_color', PURPLE_C),
                         fill_opacity=kwargs.get('fill_opacity', 0.9),
                         side_length=side_length,
                         **kwargs)
        self.corner_radius = side_length * 0.05
        self.round_corners(self.corner_radius)


class Semibreve(Breve):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rotate(PI / 4)


class Minim(Polygon):
    def __init__(self, **kwargs):
        super().__init__(
            [-0.5,  0.0, 0],
            [-0.05, 0.5, 0],
            [-0.05, 1.5, 0],
            [ 0.05, 1.5, 0],
            [ 0.05, 0.5, 0],
            [ 0.5,  0.0, 0],
            [ 0.0, -0.5, 0],
            color=kwargs.get('color', PURPLE_C),
            fill_color=kwargs.get('fill_color', PURPLE_C),
            fill_opacity=kwargs.get('fill_opacity', 0.9),
            **kwargs)
        self.corner_radius = 0.05
        self.round_corners(self.corner_radius)
        self.shift(self.get_center())

    def get_critical_point(self, direction):
        if np.array_equal(direction, [0, 0, 0]):
            return [0, 0, 0]
        return super().get_critical_point(direction)
