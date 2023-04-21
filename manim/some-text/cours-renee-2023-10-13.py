from manim import *

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


class YouTubeShort(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        # French 
        paragraph_fr = Paragraph(
            "pétard",
            "pétarade",
            "aérien",
            "aérer",
        )
        
        
        paragraph_phonetics_fr = Paragraph(
            "[petaʀ]",
            "[petaʀad]",
            "[aeʀjɛ̃, jɛn]",
            "[aeʀe]"
        )
        
            
        # English 
        paragraph_en = Paragraph(
            "firecracker",
            "banging",
            "aerial",
            "ventilate",
        )
        
        
        paragraph_phonetics_en = Paragraph(
            "/ˈfaɪərkrækər/",
            "/ˈbæŋɪŋ/",
            "/ˈɛəriəl/",
            "/ˈvɛntɪleɪt/"
        )
        
    
        
        

        # Displaying text
        self.play(Write(paragraph_fr))
        self.wait(6)


        self.play(
            ReplacementTransform(
                paragraph_fr,
                paragraph_phonetics_fr
            )
        )
        self.wait(6)

        self.play(FadeOut(paragraph_phonetics_fr))
        self.wait(2)

        self.play(Write(paragraph_en)
        )
        self.wait(6)

        self.play(
            ReplacementTransform(
                paragraph_en,
                paragraph_phonetics_en
            )
        )
        self.wait(6)

        

        
