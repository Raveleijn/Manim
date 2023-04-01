from manim import *
import numpy as np
from colour import Color

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

class RateFunc(Scene):
    def construct(self):
        polys = VGroup(*[RegularPolygon(i+3, radius=1, fill_opacity=0.5, color=Color(hue=i/10, saturation=1, luminance=0.5)) for i in range(5)]).arrange(RIGHT)
        self.play(Create(polys))
        self.play(
            Rotate(polys[0], PI, rate_func=lambda t: t), # rate_func=linear
            Rotate(polys[1], PI, rate_func=smooth),  # default behavior for most animations
            Rotate(polys[2], PI, rate_func=lambda t: np.sin(t*PI)),
            Rotate(polys[3], PI, rate_func=there_and_back),
            Rotate(polys[4], PI, rate_func=lambda t: 1 - abs(1-1.5*t)),
            run_time=2
        )
        self.wait()

class SimpleCustomAnimation(Scene):
    def construct(self):
        def spiral_out(mobject, t):
            radius = 4 * t
            angle = 2*t * 2*PI
            mobject.move_to(radius*(np.cos(angle)*RIGHT + np.sin(angle)*UP))
            mobject.set_color(Color(hue=t, saturation=1, luminance=0.5))
            mobject.set_opacity(1-t)
        
        d = Dot(color=YELLOW)
        self.add(d)
        self.play(UpdateFromAlphaFunc(d, spiral_out, run_time=3))

class Disperse(Animation):
    def __init__(self, mobject, dot_radius=0.05, dot_number=100, **kwargs):
        super().__init__(mobject, **kwargs)
        self.dot_radius = dot_radius
        self.dot_number = dot_number
    
    def begin(self):
        dots = VGroup(
            *[Dot(radius=self.dot_radius).move_to(self.mobject.point_from_proportion(p))
              for p in np.linspace(0, 1, self.dot_number)]
        )
        for dot in dots:
            dot.initial_position = dot.get_center()
            dot.shift_vector = 2*(dot.get_center() - self.mobject.get_center())
        dots.set_opacity(0)
        self.mobject.add(dots)
        self.dots = dots
        super().begin()
        
    def clean_up_from_scene(self, scene):
        super().clean_up_from_scene(scene)
        scene.remove(self.dots)

    def interpolate_mobject(self, alpha):
        alpha = self.rate_func(alpha)  # manually apply rate function
        if alpha <= 0.5:
            self.mobject.set_opacity(1 - 2*alpha, family=False)
            self.dots.set_opacity(2*alpha)
        else:
            self.mobject.set_opacity(0)
            self.dots.set_opacity(2*(1 - alpha))
            for dot in self.dots:
                dot.move_to(dot.initial_position + 2*(alpha-0.5)*dot.shift_vector)
            
            

class CustomAnimationExample(Scene):
    def construct(self):
        st = Star(color=YELLOW, fill_opacity=1).scale(3)
        self.add(st)
        self.wait()
        self.play(Disperse(st, dot_number=200, run_time=4))