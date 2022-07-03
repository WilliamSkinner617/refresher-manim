from manim import *
from random import randrange

# Specifying the home directory for .svg imports

HOME = r"C:\Users\Will\Downloads"

# First, we create a class

# A class is a code template for creating objects, which have member variables and have behaviour associated with them.

class Test_1(Scene):

# We then define the function construct(self) - a function is a group of related statements that perform a specific task.

    def construct(self):

# Stage 1 - Construct your shapes

        circ = Circle(radius=2.4,color=RED, fill_opacity=1)

# Stage 2 - Animate your shapes

        self.play(DrawBorderThenFill(circ))

# Again, we need to put the following at the start every time:

class Test_2(Scene):

    def construct(self):

# Now, if you have loaded the Manim library into your IDE or text editor, it should recommend some kwargs

# However, some are more general and may not be displayed (e.g., fill_color, fill_opacity).

# Step 1 - Object creation

        sq = Square(
            side_length=1, stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.75
        )

# Step 2 - Object animation. Now, we want to animate or 'create' the object we have created in step 1.
# There are many different options for how we do this - check Manim documentation.

        self.play(Create(sq), run_time=3)

# Above, we specified how long the animation would run for with the kwarg 'run_time'.

        self.wait()

# self.wait() asks for a pause after the animation - the default value is 1 unless specified inside the brackets.

class Test_3(Scene):

    def construct(self):

# MObjects can be positioned using .to_edge, where we specify which edge (e.g., L, R) and the buffer.

        text = Tex("Hello").to_edge(UL, buff=1)

# To move objects, we can use .shift(DIRECTION * X)

        sq = Square(side_length=1, fill_color=BLUE, fill_opacity=1).shift(LEFT * 3)

# To reduce the size of a MObject, you can use .scale(X)

        tri = Triangle().scale(0.6).to_edge(DR)

        self.play(Write(text))

        self.play(DrawBorderThenFill(sq), run_time=2)

        self.play(Create(tri))

        self.wait()

        self.play(text.animate.to_edge(UR), run_time=2)

        self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time=3)

        self.wait()

class Test_4(Scene):
    def construct(self):

        ax = Axes()

        vec = Vector(direction=[1,3,0], stroke_width=2, tip_length=0.4, stroke_color=RED)

        self.play(DrawBorderThenFill(ax), run_time=3)

        self.play(DrawBorderThenFill(vec), run_time=3)

        self.wait()

class Test_5(Scene):
    def construct(self):

        rect = Rectangle(height=2, width=1, fill_color=BLUE_E, stroke_color=BLUE_E, fill_opacity=1).to_edge(UR)

        circ = Circle(radius=0.5, fill_color=BLUE_A, stroke_color=BLUE_A, fill_opacity=1).to_edge(DL)

        arrow = always_redraw(
            lambda : Line(
                start=rect.get_bottom(), end=circ.get_top(), buff=0.2
            ).add_tip()
        )

        mobjects = VGroup(rect, circ, arrow)

        self.play(Create(mobjects), run_time=3)

        self.wait()

        self.play(rect.animate.to_edge(UL), circ.animate.to_edge(DR), run_time=2)

        self.wait()

        self.play(rect.animate.scale(0.5), circ.animate.scale(2), run_time=2)

        self.wait()

class Test_6(Scene):
    def construct(self):

        num = MathTex("ln(2)").set_color(WHITE)

        box = always_redraw(
            lambda : SurroundingRectangle(
                num, stroke_color=BLUE, fill_color=RED, fill_opacity=0.2, buff=0.5
            )
        )

        text = always_redraw(
            lambda:Tex(
                "Text"
            ).next_to(box, DOWN, buff=0.25)
        )

        mobjects = VGroup(num, box, text)

        self.play(DrawBorderThenFill(mobjects), run_time=3)
        self.play(num.animate.shift(RIGHT*2), run_time=2)
        self.wait()

class Test_7(Scene):
    def construct(self):

        # Create value tracker

        k = ValueTracker(0)

        num = always_redraw(
            lambda: DecimalNumber().set_value(k.get_value())
        )

        self.play(FadeIn(num))
        self.wait()
        self.play(k.animate.set_value(5), run_time=3, rate_func=smooth)
        self.play(k.animate.set_value(0), run_time=3, rate_func=smooth)
        self.wait()

class Test_8(Scene):

    def construct(self):

        plane = NumberPlane(
            x_range=[-4, 4, 2], x_length=8, y_range=[0,16,4], y_length=8
        ).to_edge(DOWN).add_coordinates()

        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")

        parab = plane.plot(
            lambda x: x**2, color=GREEN
        )

        self.play(DrawBorderThenFill(plane, labels))
        self.play(Create(parab))
        self.wait()

class ResolvingVectors(Scene):

    def construct(self):

# Set background colour to white (default is black)

        self.camera.background_color = WHITE

# Create the base line - the positioning of the 'Line' class is specified with a start and an end.

        baseline = DashedLine(start=[-0.5, 0, 0], end=[+2, 0, 0], stroke_width=1, stroke_color=BLACK).shift(1*DOWN)

# Create the vector - the positioning of the 'Vector' class is specified with a direction.

        vec = Vector(direction=[2, 3, 0], stroke_width=2, tip_length=0.4, stroke_color=BLACK).shift(1*DOWN, 0.5*LEFT)

# Create the label for the vector - this requires MathTex, where equations are written in a similar manner to latex
# (But two slashes instead of one)

        vec_label = MathTex("\\vec{v}").next_to(vec, RIGHT, buff=0.4).set_color(BLACK).shift(1.4*UP)

# Create the horizontal component of the vector

        hor_comp = Vector(direction=[2, 0, 0], stroke_width=1.5, stroke_color=BLUE, tip_length=0.4).shift(1*DOWN, 0.5*LEFT)

# Create the label for the horizontal component

        hor_comp_label = MathTex("\\vec{v}_h").next_to(hor_comp, DOWN, buff=0.2).set_color(BLUE)

# Create the vertical component of the vector

        ver_comp = Vector(direction=[0, 3, 0], stroke_width=1.5, stroke_color=BLUE, tip_length=0.4).shift(1*DOWN, 1.5*RIGHT)

# Create the label for the vertical component

        ver_comp_label = MathTex("\\vec{v}_v").next_to(ver_comp, LEFT, buff=0.2).set_color(BLUE)

# Create the angle (the position of the 'Angle' class is specified by the two lines/vectors that we want to draw an angle between, and a radius.

        theta = Angle(hor_comp, vec, radius=0.4, stroke_width=1, stroke_color=RED)

# Creat the theta angle label

        theta_label = MathTex("\\theta").next_to(theta, RIGHT, buff=0.2).set_color(RED).shift(0.2*UP)

# The first line of equations - looking at the horizontal component

        first_line = MathTex("|{{\\vec{v}_h}}|=|{{\\vec{v}}}|cos({{\\theta}})").set_color(BLACK).shift(4*RIGHT, 1*UP)

# Setting various specific parts of the equation to be specific colours

        first_line.set_color_by_tex("\\vec{v}_h", color=BLUE, substring=False)

        first_line.set_color_by_tex("\\vec{v}", color=BLACK, substring=False)

        first_line.set_color_by_tex("\\theta", color=RED, substring=False)

# The second line of equations - looking at the vertical component

        second_line = MathTex("|{{\\vec{v}_v}}|=|{{\\vec{v}}}|sin({{\\theta}})").set_color(BLACK).next_to(first_line, DOWN)

# Setting various specific parts of the equation to be specific colours

        second_line.set_color_by_tex("\\vec{v}_v", color=BLUE, substring=False)

        second_line.set_color_by_tex("\\vec{v}", color=BLACK, substring=False)

        second_line.set_color_by_tex("\\theta", color=RED, substring=False)

# Now, we make a VGroup (vec_resolve) to group all of these different objects so we can act on them all at once.

        vec_resolve = VGroup(baseline, vec, vec_label, hor_comp, hor_comp_label, ver_comp, ver_comp_label, theta,
                             theta_label, first_line, second_line)

# Here, we create the target that we will use later to shift the focus to the centre and scale up the point of interest

        vec_resolve.generate_target()
        vec_resolve.target.shift(2.5 * LEFT)

# Now, we animate in the desired order.

        self.play(DrawBorderThenFill(vec), run_time=2)

        self.play(DrawBorderThenFill(vec_label), run_time=0.5)

        self.play(DrawBorderThenFill(baseline), run_time=2)

        self.play(DrawBorderThenFill(theta), run_time=2)

        self.play(Write(theta_label), run_time=0.5)

        self.play(DrawBorderThenFill(hor_comp), run_time=2)

        self.play(Write(hor_comp_label), run_time=0.5)

        self.play(Write(first_line), run_time=3)

        self.play(DrawBorderThenFill(ver_comp), run_time=2)

        self.play(Write(ver_comp_label), run_time=0.5)

        self.play(Write(second_line), run_time=3)

        self.play(MoveToTarget(vec_resolve),run_time=2)

        self.play(ScaleInPlace(vec_resolve, 1.6))

        self.wait(4)

        self.play(FadeOut(vec_resolve), run_time=5)