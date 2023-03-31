from manim import *
import numpy as np

class Pythagoras(Scene):
    def construct(self):
        triangle = Polygon([0,0,0], [1.5,0,0], [0,2,0])
        center = triangle.get_center_of_mass()
        triangle1 = Polygon([0,0,0], [1.5,0,0], [0,2,0])
        triangle2 = Polygon([0,0,0], [1,0,0], [0,3,0])
        triangle3 = Polygon([0,0,0], [3,0,0], [0,1,0])
        triangle.shift([-center[0],-center[1],-center[2]])
        triangle1.shift([-center[0],-center[1],-center[2]])
        triangle2.shift([-center[0],-center[1],-center[2]])
        triangle3.shift([-center[0],-center[1],-center[2]])
        self.play(Create(triangle))
        self.wait()
        self.play(Transform(triangle, triangle2))
        self.play(Transform(triangle, triangle3))
        self.play(Transform(triangle, triangle1))
        self.wait()
        self.play(Uncreate(triangle))
        self.wait()

class Graph(Scene):
    def construct(self):
        ax = Axes(x_range=(-5,5), y_range=(-1,5))
        curve = ax.plot(lambda x: x**2-1, color=GREEN)
        area = ax.get_area(curve, x_range=(0,2))
        self.add(ax)
        self.play(Create(curve))
        self.play(FadeIn(area))
        self.wait()


class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        self.wait()
        
        square = Square().move_to([2,1,0])
        c1 = Circle(radius=2, color=RED, fill_opacity=0.5)
        c1.align_to(square, UP + RIGHT + RIGHT)
        self.add(square, c1)
        self.wait()
