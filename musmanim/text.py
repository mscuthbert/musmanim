import manim as m

MAXIMA = ''
LONGA = ''
BREVE = ''
SEMIBREVE = ''
MINIM = ''


class Text(m.Text):
    def __init__(self, t, font='Adobe Garamond Pro', color=m.WHITE, **kwargs):
        super().__init__(t, font=font, **kwargs)
        self.set_color(color)


class Bravura(Text):
    def __init__(self, t='', font_size=144, color=m.PURPLE_C, **kwargs):
        super().__init__(t,
                         color=color,
                         font_size=font_size,
                         font='Bravura Text',
                         **kwargs)


def time_signature(numerator: int = 4, denominator: int = 4, **kwargs) -> m.VGroup:
    # in case we need it later...
    #     @staticmethod
    #     def numerate(digit):
    #         return '\ue09e' + chr(57472 + digit)
    #     @staticmethod
    #     def denominate(digit):
    #         return '\ue09f' + chr(57472 + digit)

    dig = lambda i: chr(57472 + i)
    num_last_digit = Bravura(dig(numerator % 10), **kwargs)
    den_last_digit = Bravura(dig(denominator % 10), **kwargs)

    if numerator >= 10:
        numerator_text = m.VGroup(Bravura(dig(numerator // 10), **kwargs),
                                  num_last_digit,
                                  ).arrange(m.RIGHT, buff=0)
    else:
        numerator_text = num_last_digit
    if denominator >= 10:
        denominator_text = m.VGroup(Bravura(dig(denominator // 10), **kwargs),
                                    den_last_digit,
                                    ).arrange(m.RIGHT, buff=0)
    else:
        denominator_text = den_last_digit
    return m.VGroup(numerator_text, denominator_text).arrange(m.DOWN, buff=0)
