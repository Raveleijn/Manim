from manim import *
import numpy as np

class ThalesTriangle(Scene):
    def construct(self):
        vt = ValueTracker(0)

        A = Dot(np.array([-2,0,0]))
        A_label = Text('A', font_size=30)
        A_label.add_updater(lambda mob:
            mob.next_to(A, DOWN)
        )

        B = Dot(np.array([2,0,0]))
        B_label = Text('B', font_size=30)
        B_label.add_updater(lambda mob:
            mob.next_to(B, DOWN)
        )

        M = Dot(np.array([(A.get_center()[0]+B.get_center()[0])/2,
                          (A.get_center()[1]+B.get_center()[1])/2,
                          (A.get_center()[2]+B.get_center()[2])/2]))
        M_label = Text('M', font_size=30)
        M_label.add_updater(lambda mob:
            mob.next_to(M, DOWN)
        )

        r = np.linalg.norm(A.get_center()-B.get_center())*0.5

        C = always_redraw(lambda:
            Dot([M.get_center()[0]+r*np.cos(vt.get_value()*PI),M.get_center()[1]+r*np.sin(vt.get_value()*PI),M.get_center()[2]])
        )
        C_label = Text('C', font_size=30)
        C_label.add_updater(lambda mob:
            mob.next_to(C, UP)
        )

        line1 = always_redraw(lambda:
            Line(C.get_center(), A.get_center())
        )
        
        line2 = always_redraw(lambda:
            Line(C.get_center(), B.get_center())
        )

        circ = Circle(radius = r).move_to(M).set_z_index(-1)

        def RightAngleDraw():
            min_distance = min([np.linalg.norm(C.get_center()-I.get_center()) for I in [A,B]])
            if min_distance < 0.001:
                return Dot(fill_opacity=0)
            else:
                return RightAngle(line1, line2, length = min(min_distance, 0.2))


        right_angle = always_redraw(RightAngleDraw)

        line3 = Line(A.get_center(), B.get_center(), color=DARK_BLUE)

        self.play(Create(A),
                  Create(B),
                  Create(line3),
                  Create(M),
                  Create(A_label),
                  Create(B_label),
                  Create(M_label))
        self.play(Create(circ))
        self.play(Create(C),
                  Create(C_label),
                  Create(line1),
                  Create(line2))
        self.add(right_angle)
        self.play(vt.animate.set_value(1.5), run_time=3)
        self.wait(0.25)
        self.play(vt.animate.set_value(0.25), run_time=3)
        self.wait()