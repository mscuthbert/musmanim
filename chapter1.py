from musmanim import *


class Scene1(Scene):
    def construct(self):
        self.wait()
        medieval_notation = MarkupText(
            '<span size="x-large">Medieval</span> '
            '<span size="x-small">and Renaissance</span> '
            '<span size="x-large">Notation</span>',
            color=YELLOW,
            font_size=32,
        ).to_edge(UP).shift(DOWN)
        self.play(Write(medieval_notation))

        credit = Text('Michael Scott Asato Cuthbert', font_size=24, fill_opacity=0.5)
        credit.to_corner(DOWN + RIGHT, buff=0.5)
        self.play(FadeIn(credit))
        self.wait(5)

        objs = [
            Maxima().shift(LEFT * 2.5),
            Longa().shift(LEFT * 2.0),
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
        self.play(Write(vg), run_time=2)

        chapter_title = Text(
            'Chapter 1: Breves and Longas',
            color=WHITE,
        ).shift(UP)
        chapter_title.z_index = 1
        self.play(Write(chapter_title),)
        self.wait(2)


class Scene2(Scene):
    def construct(self):
        num = Integer(2022, group_with_commas=False)
        vt = ValueTracker(2022)
        num.add_updater(lambda this: this.set_value(vt.get_value()))
        self.play(FadeIn(num),
                  )
        self.wait(10)
        self.play(vt.animate.set_value(1270), run_time=14)
        self.wait(4.5)
        self.play(vt.animate.set_value(850), run_time=1.5)
        self.wait(0.5)
        self.play(vt.animate.set_value(1600), run_time=1.5)
        self.wait(0.5)
        self.play(vt.animate.set_value(1270), run_time=1.5)
        self.wait()
        self.play(num.animate.shift(UP * 2))
        self.wait()
        breve = Breve()
        breve_text = Text('Breve', fill_opacity=0, stroke_opacity=0).align_to(breve, LEFT)
        vg = VGroup(breve, breve_text)
        self.play(FadeIn(breve, time=4))
        self.wait()
        self.play(vg.animate.arrange(LEFT*2))
        self.wait()
        self.play(breve_text.animate.set_opacity(1.0))
        self.wait()
        brevis = Text('Brevis', slant=ITALIC, color=YELLOW).align_to(vg, DOWN + LEFT).shift(DOWN/2)
        short = Text('“Short”', color=YELLOW).align_to(brevis, DOWN + LEFT).shift(DOWN * .8 + LEFT * .2)
        self.play(Write(brevis))
        self.wait()
        self.play(Write(short))
        self.wait(5)
        modern_breve = Bravura('', color=WHITE)
        or_text = Text('or')
        modern_breve2 = Bravura('', color=WHITE)
        modern_group = VGroup(
            modern_breve, or_text, modern_breve2
        ).arrange(RIGHT).shift(RIGHT*4, DOWN*2)
        self.play(FadeIn(modern_group))
        self.wait(3)
        self.play(FadeOut(modern_group))
        self.wait(2)
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
        self.wait(3)

        tempus = BraceBetweenPoints(nl.ticks[0].get_right(), nl.ticks[1].get_left())
        tempus_text = Text('1').next_to(tempus, DOWN)
        tempus_g = VGroup(tempus, tempus_text).align_to(vg)
        self.play(FadeIn(tempus_g))
        self.wait(5)
        ts = Bravura('', color=WHITE, font_size=60)  # TS 4/4
        qtr = Bravura('♩', color=WHITE, font_size=60)
        analogy_g = VGroup(ts, qtr).arrange(RIGHT).align_to(breve2)
        breve3 = breve2.copy()
        self.play(ReplacementTransform(breve2, analogy_g))
        self.wait(3)

        qtr_brace = Brace(analogy_g, UP)
        qtr_brace_text = Text('1').next_to(qtr_brace, UP)
        qtr_brace_group = VGroup(qtr_brace, qtr_brace_text).next_to(analogy_g, UP).shift(DOWN * .2)
        self.play(Write(qtr_brace_group))
        self.wait(3)
        beat = Text('beat').next_to(qtr_brace_text, RIGHT)
        self.play(Write(beat))

        self.wait(4)
        self.play(AnimationGroup(
                    Unwrite(beat),
                    Unwrite(qtr_brace_group),
                    ReplacementTransform(analogy_g, breve3),
                    lag_ratio=0.4),
                  )
        self.wait(3)
        tempus_tt = Text('1 tempus').next_to(tempus, DOWN)
        tempus_g_2 = tempus_g - tempus_text + tempus_tt
        self.play(ReplacementTransform(tempus_g, tempus_g_2))

        breve_last = breve3
        tempus_g_last = tempus_g_2
        breves = [breve3]
        for i in range(5):
            breve_next = breve_last.copy().next_to(breve_last, RIGHT).shift(LEFT * 0.05)
            tempus_next = BraceBetweenPoints(nl.ticks[0].get_right(), nl.ticks[i + 2].get_left())
            tempus_text_next = Text(f'{i + 2} tempora').next_to(tempus_next, DOWN)
            tempus_g_next = VGroup(
                tempus_next, tempus_text_next
            ).next_to(nl, DOWN).align_to(nl, LEFT)

            if i <= 1:
                self.play(FadeIn(breve_next))
                self.play(ReplacementTransform(tempus_g_last, tempus_g_next))
            else:
                self.play(
                    FadeIn(breve_next),
                    ReplacementTransform(tempus_g_last, tempus_g_next),
                    run_time=1-(0.1*i),
                )
            breves.append(breve_next)
            breve_last = breve_next
            tempus_g_last = tempus_g_next
        self.wait(3)
        self.play(num.animate.set_y(10))
        self.remove(num)
        self.wait(4)
        longa = Longa(rounded=False).next_to(breves[3], UP)
        self.play(FadeIn(longa))
        self.wait(2)
        longa_text_eng = Text('Long').next_to(longa, LEFT).align_to(longa, UP).shift(UP*0.2)
        self.play(Write(longa_text_eng))
        self.wait(3)
        longa_text_lat = Text('Longa', slant=ITALIC, color=YELLOW
                              ).next_to(longa_text_eng, DOWN * 0.8)
        self.play(Write(longa_text_lat))
        longa_text_quotes = Text('“Long”', color=YELLOW).next_to(longa_text_lat, DOWN * 0.8)
        self.play(Write(longa_text_quotes))

        self.wait(3)
        longa_sentence = Text('The longest long among the longs is a very long note.',
                              font_size=32, slant=ITALIC).to_corner(UR)
        self.play(Write(longa_sentence))
        self.wait()
        self.play(FadeOut(longa_sentence),
                  Unwrite(longa_text_eng),
                  Unwrite(longa_text_quotes),
                  longa_text_lat.animate.shift(UP * .2),)
        self.wait(2)

        longa_original_points = longa.get_all_points()[:]
        head_bottom = longa_original_points[-5][1]
        longa_as_brevis = [
            np.array((ll[0], max(ll[1], head_bottom), ll[2]))
            for ll in longa_original_points
        ]
        for i in range(2):
            self.play(longa.animate.set_points(longa_as_brevis), run_time=1/(i+1))
            self.wait(0.5)
            self.play(longa.animate.set_points(longa_original_points), run_time=1/(i+1))
        longa_real = Longa().next_to(breves[3], UP)
        self.play(ReplacementTransform(longa, longa_real),
                  Unwrite(longa_text_lat))
        longa = longa_real
        self.play(longa.animate.set_x(breves[0].get_x()))
        self.wait()
        arrow1 = Line(longa.get_right() + [0.3, 0.2, 0],
                      longa.get_right() + [1.3, 0.2, 0]).add_tip()
        arrow2 = Line(longa.get_right() + [0.3, 0.2, 0],
                      longa.get_right() + [0.6, 0.2, 0]).add_tip()
        arrow3 = Line(longa.get_right() + [0.3, 0.2, 0],
                      longa.get_right() + [4.8, 0.2, 0]).add_tip()
        arrow4 = Line(longa.get_right() + [0.3, 0.2, 0],
                      longa.get_right() + [1.8, 0.2, 0]).add_tip()

        self.play(GrowFromPoint(arrow1, arrow1.get_start()))
        self.play(ReplacementTransform(arrow1, arrow2))
        self.play(ReplacementTransform(arrow2, arrow3), run_time=0.6)
        self.play(ReplacementTransform(arrow3, arrow4), run_time=0.4)
        self.wait()
        question_mark = Text('?').next_to(arrow4, RIGHT)
        self.play(FadeIn(question_mark))
        self.wait()


class Scene3(Scene):
    def construct(self):
        breve = Breve().shift(UP * 1.5)
        longa = Longa().next_to(breve, DOWN * 3)
        self.play(FadeIn(longa, breve))
        title = MarkupText(
            f'How long is a <span fgcolor="{YELLOW}"><i>longa</i></span>?'
        ).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        self.play(breve.animate.shift(LEFT * 2),
                  longa.animate.shift(LEFT * 2),
                  )
        qtr = Bravura('', color=WHITE, font_size=120).next_to(breve, RIGHT).shift(RIGHT * 2 + UP * .3)
        self.play(FadeIn(qtr))
        self.wait(2)
        half = Bravura('', color=WHITE, font_size=120).next_to(longa, RIGHT).shift(RIGHT * 2)
        self.play(FadeIn(half))
        self.wait(2)
        ts = time_signature(4, 4, color=WHITE).shift(UP * .4 + LEFT * .2)
        self.play(FadeIn(ts))
        t1 = MarkupText(f'<span fgcolor="{YELLOW}">1</span> beat').next_to(qtr, RIGHT)
        t2 = MarkupText(f'<span fgcolor="{YELLOW}">2</span> beats').next_to(half, RIGHT)
        self.play(FadeIn(t1, t2))
        self.wait(3)
        t1b = MarkupText(f'<span fgcolor="{YELLOW}">2</span> beats').next_to(qtr, RIGHT)
        t2b = MarkupText(f'<span fgcolor="{YELLOW}">4</span> beats').next_to(half, RIGHT)
        ts2 = time_signature(3, 8, color=WHITE).shift(UP * .4 + LEFT * .2)
        self.play(ReplacementTransform(t1, t1b),
                  ReplacementTransform(t2, t2b),
                  ReplacementTransform(ts, ts2),
                  )
        self.wait(7)
        t1c = MarkupText(f'<span fgcolor="{YELLOW}">4</span> beats').next_to(qtr, RIGHT)
        t2c = MarkupText(f'<span fgcolor="{YELLOW}">8</span> beats').next_to(half, RIGHT)
        ts3 = time_signature(12, 16, color=WHITE).shift(UP * .4 + LEFT * .2)
        self.play(ReplacementTransform(t1b, t1c),
                  ReplacementTransform(t2b, t2c),
                  ReplacementTransform(ts2, ts3),
                  )
        self.wait(5)
        ts_strange = time_signature(79, 41, color=WHITE).shift(UP * .4 + LEFT * .2)
        self.play(ReplacementTransform(ts3, ts_strange))
        t1d = MarkupText(f'<span fgcolor="{YELLOW}"><i>n</i></span> beats').next_to(qtr, RIGHT)
        t2d = MarkupText(f'<span fgcolor="{YELLOW}">2<i>n</i></span> beats').next_to(half, RIGHT)
        self.play(ReplacementTransform(t1c, t1d),
                  ReplacementTransform(t2c, t2d),
                  )

        self.wait(6)
        self.play(FadeOut(t1d, t2d, qtr, half, ts_strange))
        self.wait(2)

        one_tempus = MarkupText(
            f'<span fgcolor="{YELLOW}">1</span> <i>tempus</i>').next_to(breve, RIGHT).shift(RIGHT)
        three_temp = MarkupText(
            f'<span fgcolor="{YELLOW}" underline="double" underline_color="{PURPLE}">3</span> <i>tempora</i>'
        ).next_to(longa, RIGHT).shift(RIGHT + UP * .2)
        self.play(Write(one_tempus))
        self.wait(4)
        self.play(Write(three_temp))
        self.wait(3)
        perfect = MarkupText('Perfect <i>longa</i>').next_to(longa, DOWN)
        self.play(Write(perfect))
        self.wait(4)
        # self.interactive_embed()


class Scene4_Perfection(Scene):
    def construct(self):
        title = MarkupText(
            f'<span fgcolor="{YELLOW}">Perfection</span> in medieval thought'
        ).to_edge(UP)
        self.play(Write(title))
        self.wait()
        perfect = Text('Perfect', color=YELLOW).shift(LEFT + UP * 1.5)
        self.play(FadeIn(perfect))
        self.wait()
        complete = Text('complete').next_to(perfect, RIGHT)
        complete.shift(DOWN * 0.1)   # adjust for lack of descenders in "Perfect"
        self.play(FadeIn(complete))
        self.wait()

        imperfect = Text('Imperfect', color=YELLOW).shift(LEFT + DOWN * 1.5)
        self.play(FadeIn(imperfect))
        self.wait()
        incomplete = Text('incomplete').next_to(imperfect, RIGHT)
        self.play(FadeIn(incomplete))
        self.wait(4)

        omne = Text('Omne trinum est perfectum', slant=ITALIC)
        omne.shift(UP * .25)
        self.play(Write(omne))
        self.wait()

        omne_eng = Text('Everything that comes in threes is complete')
        omne_eng.next_to(omne, DOWN, buff=0)
        self.play(Write(omne_eng))
        self.wait()
        triangle = Triangle().shift(DOWN * 0.2)
        self.play(Create(triangle),
                  FadeOut(omne, omne_eng),
                  )
        self.wait()
        vg = VGroup(perfect, complete, imperfect, incomplete)
        father = Text('Father', slant=ITALIC, font_size=32).next_to(triangle, UP, buff=0.1)
        son = Text('Son', slant=ITALIC, font_size=32).next_to(triangle, LEFT + DOWN, buff=0)
        hg = Text('Holy Spirit', slant=ITALIC, font_size=32).next_to(triangle, RIGHT + DOWN, buff=0)
        trinity = VGroup(father, son, hg)

        self.play(FadeOut(vg),
                  FadeIn(trinity),
                  )
        self.wait()
        self.play(father.animate.scale(1.5))
        self.play(father.animate.scale(1/1.5),
                  son.animate.scale(1.5),
                  )
        self.play(son.animate.scale(1/1.5),
                  hg.animate.scale(1.5),
                  )
        self.play(hg.animate.scale(1/1.5))
        self.wait()
        self.play(FadeOut(trinity, triangle))
        self.play(FadeIn(vg))
        self.wait()
        three = Text('3', slant=ITALIC).set_x(complete.get_x()).set_y(complete.get_y() + 0.1)
        self.play(ReplacementTransform(complete, three))
        self.wait(2)
        one_or_two = MarkupText('<i>1</i> or  <i>2</i>'
                                ).set_x(incomplete.get_x()).set_y(incomplete.get_y() + 0.1)
        self.play(ReplacementTransform(incomplete, one_or_two))
        self.wait(2)

        one = Text('1', font_size=60)
        one_c = one.copy()
        self.play(FadeIn(one))
        self.wait()
        circle = Circle(radius=0.5, fill_color=PURPLE_C, stroke_color=PURPLE_C, fill_opacity=0.8)
        square = Square(side_length=1, fill_color=PURPLE_C, stroke_color=PURPLE_C, fill_opacity=0.8)
        self.play(Transform(one, circle))
        self.play(Transform(circle, one_c))
        self.play(ReplacementTransform(one_c, square))
        self.wait(3)
        self.play(FadeOut(one, one_c, circle, square))
        self.wait()
        l1 = Line([1, -1.8, 0], [2.2, -1, 0], color=RED)
        l2 = Line([2.2, -1.8, 0], [1, -1, 0], color=RED)
        self.play(FadeIn(l1, l2))
        self.wait()
        two = Text('2', slant=ITALIC).next_to(imperfect, RIGHT).shift(RIGHT * .6)
        self.play(FadeOut(l1, l2),
                  ReplacementTransform(one_or_two, two)
                  )
        self.wait()
        perfect_g = VGroup(perfect, three)
        imperfect_g = VGroup(imperfect, two)
        self.play(
            perfect_g.animate.shift(DOWN),
            imperfect_g.animate.shift(UP),
        )
        self.wait()
        # self.interactive_embed()


class Scene5_Durations(Scene):
    def construct(self):
        # bounce in three breves, add to number line and play.
        br1 = Breve()
        br2 = Breve()
        br3 = Breve()
        self.play(Bounce(VGroup(br1, br2, br3).arrange(RIGHT)))
        UNIT_SIZE = br1.side_length * 1.2

        nl = NumberLine([1, 15, 1], numbers_to_include=[],
                        unit_size=UNIT_SIZE,
                        stroke_color=YELLOW).to_edge(LEFT).shift(DOWN*2 + RIGHT)
        self.play(Write(nl))
        self.play(br1.animate.move_to(to_nl(1, nl), aligned_edge=DL),
                  br2.animate.move_to(to_nl(2, nl), aligned_edge=DL),
                  br3.animate.move_to(to_nl(3, nl), aligned_edge=DL),
                  )
        self.wait()
        play_rhythm(self, [br1, br2, br3], [1.0, 1.0, 1.0])
        self.wait()

        # add a longa and put it at the end of the number line
        longa = Longa()
        self.play(Bounce(longa, above_edge=UP*2))
        self.wait()
        self.play(longa.animate.move_to(to_nl(4, nl), aligned_edge=LEFT),)
        self.wait()
        # show its length
        arrow_start = longa.get_right() + RIGHT * 0.1 + UP * .5
        longa_arrow = Arrow(arrow_start, arrow_start + RIGHT*2.6)
        self.play(GrowArrow(longa_arrow, run_time=2.5))
        self.wait()
        self.play(FadeOut(longa_arrow))

        play_rhythm(self, [br1, br2, br3, longa], [1.0, 1.0, 1.0, 3.0])
        self.wait()

        # now swap the position of the 3 breves with the longa and play.
        br_group = VGroup(br1, br2, br3)
        self.play(br_group.animate.shift(UP*1.5))
        self.play(longa.animate.move_to(to_nl(1, nl), aligned_edge=LEFT))
        self.play(br_group.animate.shift(RIGHT*3))
        self.play(br1.animate.move_to(to_nl(4, nl), aligned_edge=DL),
                  br2.animate.move_to(to_nl(5, nl), aligned_edge=DL),
                  br3.animate.move_to(to_nl(6, nl), aligned_edge=DL),
                  )
        self.wait()
        play_rhythm(self, [longa, br1, br2, br3], [3.0, 1.0, 1.0, 1.0])
        self.wait()

        # add another breve -- we'll color it blue so you can tell
        # it apart from the others.
        br4 = Breve(color=BLUE)
        self.play(Bounce(br4))

        # we want to put the new breve just before the other three.
        arc = CurvedArrow(br4.get_critical_point(UL) + LEFT*0.2 + DOWN*0.2,
                          br1.get_left() + LEFT*0.1,
                          )
        self.play(Create(arc))
        self.wait()

        # what we expect will happen is that the other three breves will
        # start one tempus later to make room for their new friend.
        expect_title = MarkupText(
            f'What we <span fgcolor="{YELLOW}"><i>expect</i></span> would happen'
        ).to_edge(UP)
        self.play(FadeIn(expect_title))
        br4_c = br4.copy()
        br_g_c = br_group.copy()
        self.add(br_g_c, br4_c)
        self.remove(br_group, br4)
        self.play(br_g_c.animate.set_opacity(0.3),
                  br4_c.animate.set_opacity(0.3),
                  FadeOut(arc),
                  )
        self.wait()
        self.play(br_g_c.animate.shift(RIGHT * UNIT_SIZE),
                  br4_c.animate.shift(LEFT*1.5),
                  )
        self.play(br4_c.animate.move_to(to_nl(4, nl), aligned_edge=DL))
        self.wait()

        # that's what we expect to happen.
        self.play(br4_c.animate.to_edge(DOWN, buff=DOWN*2),
                  br_g_c.animate.to_edge(DOWN, buff=DOWN*2),
                  FadeOut(expect_title)
                  )
        self.play(FadeIn(br4, br_group),)
        self.wait()
        actual_title = MarkupText(
            f'What <span fgcolor="{YELLOW}"><i>actually</i></span> happens'
        ).to_edge(UP)
        self.play(FadeIn(actual_title))
        self.wait()
        self.play(br4.animate.shift(LEFT*2.8))
        self.play(br4.animate.move_to(to_nl(3, nl), aligned_edge=DL))
        self.wait()
        play_rhythm(self,
                    [longa, br4, br1, br2, br3],
                    [2.0, 1.0, 1.0, 1.0, 1.0],
                    max_wiggle_time=1.0)
        self.wait()
        self.play(FadeOut(actual_title))

        longa_c = longa.copy()
        br_rep1 = Breve().move_to(to_nl(1, nl), aligned_edge=DL)
        br_rep2 = Breve().move_to(to_nl(2, nl), aligned_edge=DL)
        br_rep_g = VGroup(br_rep1, br_rep2)
        self.play(Transform(longa, br_rep_g, run_time=1.5))
        self.wait(2)
        self.play(Transform(longa, longa_c, run_time=1.5))
        imperfect_text = MarkupText('imperfect\nlonga', slant=ITALIC, font_size=32)
        imperfect_text.next_to(longa, UP).shift(RIGHT * 0.4)
        self.play(FadeIn(imperfect_text))
        self.wait()

        def move_and_arrange(vg_all: VGroup) -> VGroup:
            vg_all.arrange(RIGHT)
            vg_all.submobjects[0].shift(DOWN * 0.5)
            vg_all.move_to(ORIGIN)
            return vg_all

        vg_all_objects = VGroup(longa, br4, br1, br2, br3)
        self.play(ApplyFunction(move_and_arrange, vg_all_objects),
                  FadeOut(imperfect_text))
        self.wait()
        br4_origin = br4.get_center()
        self.play(br4.animate.to_edge(DOWN, buff=DOWN*2),
                  longa.animate.shift(RIGHT*1.2),
                  )
        self.wait()
        self.play(br4.animate.move_to(br4_origin),
                  longa.animate.shift(LEFT*1.2),
                  )
        self.wait()
        self.play(br4.animate.set_color(PURPLE_C), run_time=2.0)
        self.wait()
        self.play(br3.animate.to_edge(UP, buff=DOWN * 2),)
        self.wait()
        self.play(
            longa.animate.move_to(to_nl(1, nl), aligned_edge=LEFT),
            br4.animate.move_to(to_nl(4, nl), aligned_edge=DL),
            br1.animate.move_to(to_nl(5, nl), aligned_edge=DL),
            br2.animate.move_to(to_nl(6, nl), aligned_edge=DL),
        )
        self.wait()


class Scene6_Imperfection(Scene):
    def construct(self):
        title = MarkupText(
            f'When does <span fgcolor="{YELLOW}">Imperfection</span> occur?'
        ).to_edge(UP)
        self.play(Write(title))
        self.wait()

        br = Breve().scale(0.9)
        self.play(Bounce(br))
        self.wait(2)

        def shrink_height(points):
            return points * np.array([1, .25, 1])

        self.play(br.animate.apply_points_function_about_point(shrink_height))
        self.wait()

        # def double_width(points):
        #     return points * np.array([2, 1, 1])
        #
        # def triple_width(points):
        #     return points * np.array([3, 1, 1])

        def shrink_and_triple_width(points):
            return points * np.array([3, .25, 1])


        br2 = br.copy()
        br2.add()

        br3 = br.copy()
        br3.add()
        self.play(br2.animate.shift(LEFT),
                  br3.animate.shift(RIGHT),
                  )
        br_g = VGroup(br, br2, br3)
        self.play(br_g.animate.shift(RIGHT*2))

        longa = Longa(color=GREEN).shift(LEFT)
        br2_longa = Breve(color=GREEN).move_to(longa, ORIGIN).shift(LEFT)
        self.play(Bounce(longa, bound=-0.2))
        self.play(Transform(longa, br2_longa), run_time=0.2)
        self.play(longa.animate.apply_points_function_about_point(shrink_and_triple_width))
        self.wait()
        b_longa = Brace(longa, DOWN)
        b_br_g = Brace(br_g, DOWN)
        self.play(Write(b_longa),
                  Write(b_br_g),
                  )
        t3_perf = MarkupText('3 <i>tempora</i> = perfection', font_size=24)
        t3_perf2 = t3_perf.copy()
        t3_perf.next_to(b_longa, DOWN)
        t3_perf2.next_to(b_br_g, DOWN)
        self.play(Write(t3_perf),
                  Write(t3_perf2),
                  )
        self.wait(4)
        self.play(Unwrite(t3_perf),
                  Unwrite(t3_perf2),
                  )

        br4 = br2.copy()
        br4.set_x(ORIGIN[0] - 0.5).set_color(BLUE)
        self.play(Bounce(br4))
        self.wait()

        # confused.
        self.play(Confused(br4, run_time=4.0, num_reps=3, distance=0.25))
        self.play(Agitate(br4))

        self.wait()

        for i in range(4):
            if i == 0:
                self.play(br4.animate.next_to(br2, LEFT, buff=0.05), run_time=0.4)
            self.play(br4.animate.shift(LEFT*0.2*i), run_time=0.2 + i/10)
            self.play(br4.animate.shift(RIGHT*0.2*i), run_time=0.2 + i/10)

        self.play(
            AnimationGroup(
                br4.animate.shift(RIGHT * 0.9),
                br2.animate.shift(RIGHT),
                br.animate.shift(RIGHT),
                br3.animate.shift(RIGHT * 2),
                lag_ratio=0.2,
            )
        )

        self.wait(2)
        self.play(Circumscribe(br3, Circle, time_width=2, run_time=3, buff=0.5))
        self.play(Agitate(br3))
        self.wait(2)

        self.play(
            AnimationGroup(
                br3.animate.shift(LEFT * 2),
                br.animate.shift(LEFT),
                br2.animate.shift(LEFT),
                br4.animate.shift(LEFT * 1.5),
                lag_ratio=0.2,
            )
        )
        self.wait(2)
        # self.play(br4.animate.shift(LEFT * 0.9))
        self.play(Agitate(br4))
        self.wait()


        # breve tries to cuddle up to longa instead.


        def shrink_right_side(obj, scale_ratio, critical_point=LEFT, other_scale=1.0,
                              **animate_kwargs):
            left_side: np.ndarray = obj.get_critical_point(critical_point)
            self.play(obj.animate.apply_points_function_about_point(
                lambda points: (points - left_side) * np.array((scale_ratio, other_scale, 1)) + left_side
            ), **animate_kwargs)

        self.play(br4.animate.next_to(longa, RIGHT, buff=0.05), run_time=0.4)
        self.wait()
        shrink_right_side(longa, .9)
        self.play(Agitate(br4, num_reps=1))
        self.play(br4.animate.next_to(longa, RIGHT, buff=0.05), run_time=0.4)
        self.wait(0.5)
        shrink_right_side(longa, .9, run_time=0.5)
        self.play(Agitate(br4, num_reps=1), run_time=0.3)
        self.play(br4.animate.next_to(longa, RIGHT, buff=0.05), run_time=0.2)

        remainder = (2/3) / (.9*.9)  # get to 2/3
        shrink_right_side(longa, remainder, run_time=0.5)
        self.play(br4.animate.next_to(longa, RIGHT, buff=0.05), run_time=0.2)
        self.wait()
        self.play(Agitate(VGroup(longa, br4)))
        self.wait(3)

        # now with breve at top.

        def shrink_left_side(obj, scale_ratio, **animate_kwargs):
            right_side: np.ndarray = obj.get_right()
            self.play(obj.animate.apply_points_function_about_point(
                lambda points: (points - right_side) * np.array((scale_ratio, 1, 1)) + right_side
            ), **animate_kwargs)

        self.play(br4.animate.shift(UP))
        self.wait()
        shrink_right_side(longa, 1.5)  # grow, actually...
        self.wait()
        self.play(br4.animate.align_to(longa, LEFT))
        self.wait()
        shrink_left_side(longa, 2/3)
        self.play(br4.animate.next_to(longa, LEFT, buff=0.05))
        self.wait(4)
        perf_g1 = VGroup(b_longa, br4, longa)
        perf_g2 = VGroup(b_br_g, br_g)
        self.play(perf_g1.animate.shift(RIGHT*3),
                  perf_g2.animate.shift(RIGHT*2),
                  )
        self.wait()

        longa2 = Longa(color=GREEN).shift(LEFT*3)
        self.play(Bounce(longa2, bound=-0.2))
        br2_longa2 = Breve(color=GREEN).set_x(longa2.get_x()).set_y(longa2.get_y())
        self.play(Transform(longa2, br2_longa2), run_time=0.2)
        shrink_right_side(longa2, 3.0, RIGHT, 0.25, run_time=0.5)
        self.play(longa2.animate.shift(UP*.2), run_time=0.2)
        self.wait()
        b_longa2 = Brace(longa2, DOWN)
        self.play(FadeIn(b_longa2))
        self.wait(3)

        self.play(Agitate(br4))
        self.wait(4)
        shrink_right_side(longa2, 2/3, run_time=0.5)
        self.play(br4.animate.next_to(longa2, RIGHT, buff=0.05))
        shrink_left_side(longa, 3/2, run_time=0.5)
        self.wait()

        perf_1 = VGroup(longa2, br4, b_longa2)
        perf_2 = VGroup(longa, b_longa)
        perf_3 = VGroup(br2, br, br3, b_br_g)
        all_gr = VGroup(perf_1, perf_2, perf_3)

        self.play(all_gr.animate.scale(0.8))
        self.play(perf_3.animate.shift(RIGHT),
                  perf_2.animate.shift(RIGHT*1.6),
                  perf_1.animate.shift(RIGHT*2.2),
                  )
        self.wait()

        # drop in another perfect long.
        longa3 = longa.copy().next_to(perf_1, LEFT, buff=0.2)
        self.play(Bounce(longa3))
        b_longa3 = b_longa.copy().next_to(longa3, DOWN)
        self.play(FadeIn(b_longa3),
                  longa3.animate.shift(DOWN * 0.05),
                  run_time=0.5)
        self.wait(2)

        self.play(br4.animate.shift(UP * .6))
        self.wait()
        shrink_right_side(longa2, 1.5)  # grow, actually...
        shrink_right_side(longa3, 2/3)
        self.play(br4.animate.set_x(longa3.get_x() + 1))
        self.play(br4.animate.next_to(longa3, RIGHT, buff=0.05))
        self.wait(3)

        self.play(br4.animate.shift(UP * .6))
        self.wait()
        shrink_right_side(longa3, 1.5)  # grow, actually...
        self.play(br4.animate.align_to(longa3, LEFT))
        self.play(br4.animate.move_to(longa3, LEFT),
                  longa3.animate.shift(RIGHT),
                  longa2.animate.shift(RIGHT),
                  longa.animate.shift(RIGHT),
                  br2.animate.shift(RIGHT),
                  br.animate.shift(RIGHT),
                  br3.animate.shift(RIGHT * 1.2),
                  b_br_g.animate.shift(RIGHT * 0.2),
                  )
        self.wait()
        self.play(Agitate(br3))
        shrink_right_side(longa, .6)
        self.play(br2.animate.shift(LEFT * .8),
                  br.animate.shift(LEFT * .8),
                  br3.animate.shift(LEFT * 1),
                  )
        self.wait()






