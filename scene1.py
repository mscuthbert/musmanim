from musmain import *


class IntroScene(Scene):
    def construct(self):
        medieval_notation = Text('Medieval Notation').to_edge(UP).shift(DOWN)
        self.play(Write(medieval_notation))

        chapter_title = Text('Chapter 1:\nIntroduction to Medieval Noteforms', color=WHITE
                     ).shift(UP)
        chapter_title.z_index = 1

        longa = Longa()
        objs = [
            Maxima().shift(LEFT * 1.5),
            Longa().shift(LEFT * 1.5),
            Breve(),
            Semibreve(),
            Minim(),
        ]
        for i in range(1, len(objs)):
            obj = objs[i]
            prev = objs[i-1]
            obj.shift(prev.get_center() + RIGHT*2)
        vg = VGroup(
            *objs
        ).shift(LEFT * 2 + DOWN * .5)

        # longa_body = Rectangle(width=1.5, height=1).shift(DOWN, -1)
        self.play(Write(vg),)
        self.play(Write(chapter_title),)
        credit = Text('Michael Scott Asato Cuthbert', font_size=24, fill_opacity=0.5)
        credit.to_corner(DOWN + RIGHT, buff=0.5)
        self.play(FadeIn(credit))
        self.wait(1)


class SecondScene(Scene):
    def construct(self):
        num = Integer(2022, group_with_commas=False)
        vt = ValueTracker(2022)
        num.add_updater(lambda this: this.set_value(vt.get_value()))
        self.play(FadeIn(num),
                  )
        self.play(vt.animate.set_value(1270), run_time=6)
        self.play(num.animate.shift(UP * 2))

        breve = Breve()
        breve_text = Text('Breve', fill_opacity=0, stroke_opacity=0).align_to(breve, LEFT)
        vg = VGroup(breve, breve_text)
        self.play(FadeIn(breve, time=4))
        self.play(vg.animate.arrange(LEFT*2))
        self.play(breve_text.animate.set_opacity(1.0))
        self.wait()
        brevis = Text('Brevis', slant=ITALIC, color=YELLOW).align_to(vg, DOWN + LEFT).shift(DOWN/2)
        short = Text('“Short”', color=YELLOW).align_to(brevis, DOWN + LEFT).shift(DOWN * .8 + LEFT * .2)
        self.play(Write(brevis))
        self.wait()
        self.play(Write(short))
        self.wait()
        self.play(FadeOut(breve_text, brevis, short))
        self.wait()
        breve2 = breve.copy()
        self.remove(breve)
        self.add(breve2)
        self.play(breve2.animate.set_x(-3))

        nl = NumberLine([0, 6, 1], numbers_to_include=[],
                        stroke_color=YELLOW).scale(1.2)
        nl.align_to(breve2, DOWN + LEFT)
        nl.shift(DOWN * 0.3 + LEFT * 0.1)
        self.play(FadeIn(nl))
        self.wait(4)

        tempus = BraceBetweenPoints(nl.ticks[0].get_right(), nl.ticks[1].get_left())
        tempus_text = Text('1').next_to(tempus, DOWN)
        tempus_g = VGroup(tempus, tempus_text).align_to(vg)
        self.play(FadeIn(tempus_g))
        self.wait()
        ts = Bravura('', color=WHITE, font_size=60)
        qtr = Bravura('♩', color=WHITE, font_size=60)
        analogy_g = VGroup(ts, qtr).arrange(RIGHT).align_to(breve2)
        breve3 = breve2.copy()
        self.play(ReplacementTransform(breve2, analogy_g))
        self.wait()

        qtr_brace = Brace(analogy_g, UP)
        qtr_brace_text = Text('1').next_to(qtr_brace, UP)
        qtr_brace_group = VGroup(qtr_brace, qtr_brace_text).next_to(analogy_g, UP).shift(DOWN * .2)
        self.play(Write(qtr_brace_group))

        self.wait(4)
        self.play(AnimationGroup(
                    Unwrite(qtr_brace_group),
                    ReplacementTransform(analogy_g, breve3),
                    lag_ratio=0.4),
                  )
        self.wait()
