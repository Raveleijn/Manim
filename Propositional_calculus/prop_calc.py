from manim import *

#Thanks a lot to Metamath

class Axioms(Scene):
    def construct(self):
        axiom_simp = MathTex(r"\vdash A\rightarrow (B\rightarrow A)").move_to(UP*2)
        axiom_frege = MathTex(r"\vdash (A\rightarrow (B\rightarrow C))\rightarrow ((A\rightarrow B))").next_to(axiom_simp, DOWN)
        axiom_transp = MathTex(r"\vdash (\neg A\rightarrow \neg B) \rightarrow (B\rightarrow A)").next_to(axiom_frege, DOWN)
        axiom_mp = MathTex(r"A, A\rightarrow B \vdash B").next_to(axiom_transp, DOWN)
        self.play(Write(axiom_simp),Write(axiom_frege),Write(axiom_transp),Write(axiom_mp))
        self.wait()