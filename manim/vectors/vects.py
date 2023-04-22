from manim import *
import manim

SCALE_FACTOR = 0.5
# flip width => height, height => width
tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height
# Change coord system dimensions
config.frame_height = config.frame_height / SCALE_FACTOR
config.frame_width = config.frame_height * 9 / 16
FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width


class distance(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        #banner = ManimBanner()
        title = Title(f"Distance avec Manim {manim.__version__}")
        self.add(title)

        dot1 = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        dot3 = Dot([2, -1, 0])
        
        line = Line(
            dot1.get_center(),
            dot2.get_center()
        ).set_color(ORANGE)
        
        horiz_line = Line(
            dot1.get_center(),
            dot3.get_center()
        ).set_color(BLUE)
        horizontal_brace = Brace(horiz_line)
        horizontal_bracetext = horizontal_brace.get_tex("x_2 - x_1")
        
        vert_line = Line(
            dot2.get_center(),
            dot3.get_center()
        ).set_color(RED)
        vertical_brace = Brace(
            vert_line,
            direction=vert_line.copy().rotate(PI / 2).get_unit_vector()
        )
        vertical_bracetext = vertical_brace.get_tex("y_2 - y_1")
        
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        norm = "\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}"
        b2text = b2.get_tex(norm).shift(RIGHT*2.75)

        self.play(FadeIn(line))
        self.wait(1)
        self.play(FadeIn(dot1))
        self.wait(1)
        self.play(FadeIn(dot2))
        self.wait(1)
        self.play(FadeIn(dot3))
        self.wait(1)
        self.play(FadeIn(horiz_line))
        self.wait(1)
        self.play(FadeIn(vert_line))
        self.wait(1)
        self.play(FadeIn(horizontal_brace))
        self.wait(1)
        self.play(FadeIn(vertical_brace))
        self.wait(1)
        self.play(Write(horizontal_bracetext))
        self.wait(1)
        self.play(Write(vertical_bracetext))
        self.wait(1)
        self.play(FadeIn(b2))
        self.wait(1)
        self.play(Write(b2text.rotate(PI/6.5)))
        self.wait(1)
