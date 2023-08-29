from manim import *

class Introduction(Scene):
    def construct(self):
        text = Text('Have you ever wondered what numbers a').scale(3)
        self.play(Write(text))