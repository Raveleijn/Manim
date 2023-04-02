from manim import *

class Equation(Scene):
    def construct(self):
        equation = MathTex(r"a^2-b^2", r"&=a^2-ab+ab-b^2\\", r"&=a(a-b)+b(a-b)\\", r"&=(a+b)(a-b)")
        self.play(Write(equation[0]))
        self.wait()
        self.play(Write(equation[1][0]))
        temp_latex = [
            VGroup(*equation[0][0:2]).copy(),
            VGroup(*equation[0][2:5]).copy()
        ]
        self.play(
            ClockwiseTransform(temp_latex[0], VGroup(*equation[1][1:3])),
            ClockwiseTransform(temp_latex[1], VGroup(*equation[1][-3:]))
        )
        self.add(equation[1][1:3],equation[1][-3:])
        self.remove(*temp_latex)
        self.wait()
        self.play(Write(equation[1][3:-3]))
        self.wait()
        self.play(Write(equation[2][0]))
        temp_latex = [
            equation[1][1].copy(),
            equation[1][1].copy(),
            equation[1][3].copy(),
            equation[1][4].copy(),
            equation[1][5].copy(),
            equation[1][6].copy(),
            equation[1][7].copy(),
            equation[1][8].copy(),
            equation[1][9].copy(),
            equation[1][10].copy(),
            equation[1][10].copy()
        ]
        self.play(
            ClockwiseTransform(temp_latex[0], equation[2][1]),
            ClockwiseTransform(temp_latex[3], equation[2][1])
        )
        self.play(
            ClockwiseTransform(temp_latex[1], equation[2][3]),
            ClockwiseTransform(temp_latex[2], equation[2][4]),
            ClockwiseTransform(temp_latex[4], equation[2][5]),
            FadeIn(equation[2][2],equation[2][6])
        )
        self.play(ClockwiseTransform(temp_latex[5],equation[2][7]))
        self.play(
            ClockwiseTransform(temp_latex[7], equation[2][8]),
            ClockwiseTransform(temp_latex[9], equation[2][8])
        )
        self.play(
            ClockwiseTransform(temp_latex[6], equation[2][10]),
            ClockwiseTransform(temp_latex[8], equation[2][11]),
            ClockwiseTransform(temp_latex[10], equation[2][12]),
            FadeIn(equation[2][9],equation[2][13])
        )
        self.add(equation[2][1],equation[2][3:6],equation[2][7:9],equation[2][10:13])
        self.remove(*temp_latex)
        self.wait()
        self.play(Write(equation[3][0]))
        temp_latex = [
            equation[2][1].copy(),
            VGroup(*equation[2][2:7].copy()),
            equation[2][7].copy(),
            equation[2][8].copy(),
            VGroup(*equation[2][9:14].copy())
        ]
        self.play(
            ClockwiseTransform(temp_latex[0],equation[3][2]),
            ClockwiseTransform(temp_latex[2],equation[3][3]),
            ClockwiseTransform(temp_latex[3],equation[3][4]),
            FadeIn(equation[3][1], equation[3][5])
        )
        self.play(
            ClockwiseTransform(temp_latex[1], VGroup(*equation[3][6:11])),
            ClockwiseTransform(temp_latex[4], VGroup(*equation[3][6:11]))
        )
        self.add(*equation[3][2:5],*equation[3][6:11])
        self.remove(*temp_latex)
        self.wait()


        