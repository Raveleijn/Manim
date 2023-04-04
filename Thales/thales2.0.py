from manim import *

class ProofThales(Scene):
    def construct(self):
        proportion = ValueTracker(0.25)
        diameter = Line(2*LEFT, 2*RIGHT).set_z_index(-1)
        parallell_line = Line(15*LEFT, 15*RIGHT).set_z_index(-1)
        circle = Circle(2,color=BLUE).set_z_index(-1)
        A = Dot(2*LEFT)
        M = Dot(ORIGIN)
        B = Dot(2*RIGHT)
        C = always_redraw(lambda:Dot(circle.point_at_angle(proportion.get_value()*PI)))

        line1 = always_redraw(lambda:Line(A.get_center(), C.get_center()))
        line2 = always_redraw(lambda:Line(B.get_center(), C.get_center()))

        A_label = MathTex(r'A').scale(0.75).next_to(A, LEFT)
        M_label = MathTex(r'M').scale(0.75).next_to(M, DOWN)
        B_label = MathTex(r'B').scale(0.75).next_to(B, RIGHT)
        C_label = always_redraw(lambda:MathTex(r'C').scale(0.75).next_to(C, UP))


        self.play(Create(VGroup(M,M_label)))
        self.play(Create(diameter))
        self.play(Create(VGroup(A,A_label)), Create(VGroup(B,B_label)))
        self.play(Create(circle))
        self.play(Create(VGroup(C,C_label)))
        self.play(Create(line1),Create(line2))
        self.wait()
        self.play(proportion.animate.set_value(1.75))
        self.wait()
        self.play(proportion.animate.set_value(0.75))
        self.wait()
        self.play(proportion.animate.set_value(0.25))
        self.wait()
        self.play(Transform(diameter, parallell_line))
        self.add(diameter)
        self.play(parallell_line.animate.move_to(C.get_center()))

        parallell_line.add_updater(lambda m:m.move_to(C.get_center()))
        
        self.wait()
        self.play(proportion.animate.set_value(1.75))
        self.wait()
        self.play(proportion.animate.set_value(0.75))
        self.wait()
        self.play(proportion.animate.set_value(0.25))
        self.wait()

        angle1 = always_redraw(lambda:Angle(parallell_line, line1, radius=0.5, quadrant=(-1,-1), other_angle=bool(proportion.get_value()), color=PINK))
        angle2 = always_redraw(lambda:Angle(parallell_line, line2, radius=0.5, quadrant=(1,-1), other_angle=True, color=YELLOW))
        angle1_copy = always_redraw(lambda:Angle(line1, diameter, radius=0.5, quadrant=(1,1), other_angle=True, color=PINK))
        angle2_copy = always_redraw(lambda:Angle(line2, diameter, radius=0.5, quadrant=(1,-1), other_angle=True, color=YELLOW))
        self.play(Create(angle1),Create(angle2))
        self.play(TransformFromCopy(angle1.copy(),angle1_copy),TransformFromCopy(angle2.copy(),angle2_copy))
        
        self.wait()
        self.play(proportion.animate.set_value(1.75))
        self.wait()
        self.play(proportion.animate.set_value(0.75))
        self.wait()
        self.play(proportion.animate.set_value(0.25))
        self.wait()