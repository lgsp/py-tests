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

class YouTubeShort1(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        # Russian
        line_ru_1 = Text('Привет всем.')
        #line_ru_1.to_edge(LEFT, buff=0.5).to_edge(UP, buff=0.5)
        
        phonetics_ru_1 = Text("[prʲɪˈvʲet vsʲɪm]")
        #phonetics_ru_1.to_edge(LEFT, buff=0.5).to_edge(UP, buff=0.5)
        
        line_ru_2 = Text('Давайте учить русский, ')
        phonetics_ru_2 = Text("/dəˈvajtʲɪ ʊˈtɕitʲ ˈruskʲɪj/")
        line_ru_3 = Text('английский и французский!')
        phonetics_ru_3 = Text("[ˈanɡlʲɪjskʲɪj i frant͡suzkʲɪj]")
        
        # Position second line underneath first line
        line_ru_2.next_to(line_ru_1, DOWN)
        phonetics_ru_2.next_to(phonetics_ru_1, DOWN)
        # Position third line underneath second line
        line_ru_3.next_to(line_ru_2, DOWN)
        phonetics_ru_3.next_to(phonetics_ru_2, DOWN)

        # English 
        line_en_1 = Text('Hello everybody.')
        #line_en_1.to_edge(LEFT, buff=0.5).to_edge(UP, buff=0.5)
        
        phonetics_en_1 = Text(" /hɛˈloʊ ˈɛvriˌbɑdi/")
        #phonetics_en_1.to_edge(LEFT, buff=0.5).to_edge(UP, buff=0.5)
        
        line_en_2 = Text("Let's learn Russian, ")
        phonetics_en_2 = Text(" /lɛts lɜːrn ˈrʌʃən/")
        line_en_3 = Text("English, and French!")
        phonetics_en_3 = Text("/'ɪŋɡlɪʃ, ənd frɛntʃ/")

        # Position second line underneath first line
        line_en_2.next_to(line_en_1, DOWN)
        phonetics_en_2.next_to(phonetics_en_1, DOWN)
        # Position third line underneath second line
        line_en_3.next_to(line_en_2, DOWN)
        phonetics_en_3.next_to(phonetics_en_2, DOWN)

        # French 
        line_fr_1 = Text("Bonjour tout le monde.")
        #line_fr_1.to_edge(LEFT, buff=0.5).to_edge(UP, buff=0.5)
        
        phonetics_fr_1 = Text("/bɔ̃ʒuʁ tu lə mɔ̃d")
        #phonetics_fr_1.to_edge(LEFT, buff=0.5).to_edge(UP, buff=0.5)
        
        line_fr_2 = Text("Apprenons le russe, ")
        phonetics_fr_2 = Text("/a.pʁə.nɔ̃ lə ʁys/")
        line_fr_3 = Text("l'anglais et le français !")
        phonetics_fr_3 = Text("/lɑ̃.ɡlɛ e lə fʁɑ̃.sɛ/")

        # Position second line underneath first line
        line_fr_2.next_to(line_fr_1, DOWN)
        phonetics_fr_2.next_to(phonetics_fr_1, DOWN)
        # Position third line underneath second line
        line_fr_3.next_to(line_fr_2, DOWN)
        phonetics_fr_3.next_to(phonetics_fr_2, DOWN)

        # Displaying text
        self.wait(1)
        self.play(
            Write(line_ru_1),
            Write(line_ru_2),
            Write(line_ru_3)
        )
        self.wait(6)
        
        self.play(ReplacementTransform(line_ru_1, phonetics_ru_1))
        self.play(ReplacementTransform(line_ru_2, phonetics_ru_2))
        self.play(ReplacementTransform(line_ru_3, phonetics_ru_3))
        self.wait(6)


        self.play(ReplacementTransform(phonetics_ru_1, line_en_1))
        self.play(ReplacementTransform(phonetics_ru_2, line_en_2))
        self.play(ReplacementTransform(phonetics_ru_3, line_en_3))
        self.wait(6)


        self.play(ReplacementTransform(line_en_1, phonetics_en_1))
        self.play(ReplacementTransform(line_en_2, phonetics_en_2))
        self.play(ReplacementTransform(line_en_3, phonetics_en_3))
        self.wait(6)

        self.play(ReplacementTransform(phonetics_en_1, line_fr_1))
        self.play(ReplacementTransform(phonetics_en_2, line_fr_2))
        self.play(ReplacementTransform(phonetics_en_3, line_fr_3))
        self.wait(6)

        self.play(ReplacementTransform(line_fr_1, phonetics_fr_1))
        self.play(ReplacementTransform(line_fr_2, phonetics_fr_2))
        self.play(ReplacementTransform(line_fr_3, phonetics_fr_3))
        self.wait(6)

        


class YouTubeShort2(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        # Russian
        paragraph_ru = Paragraph(
            'Привет всем.',
            'Давайте учить русский, ',
            'английский и французский!'
        )
        
        
        paragraph_phonetics_ru = Paragraph(
            "[prʲɪˈvʲet vsʲɪm]",
            "/dəˈvajtʲɪ ʊˈtɕitʲ ˈruskʲɪj/",
            "[ˈanɡlʲɪjskʲɪj i frant͡suzkʲɪj]"
        )
        

        # English 
        paragraph_en = Paragraph(
            'Hello everybody.',
            "Let's learn Russian, ",
            "English, and French!"
        )
        
        
        paragraph_phonetics_en = Paragraph(
            " /hɛˈloʊ ˈɛvriˌbɑdi/",
            " /lɛts lɜːrn ˈrʌʃən/",
            "/'ɪŋɡlɪʃ, ənd frɛntʃ/"
        )
        
        
        
        # French 
        paragraph_fr = Paragraph(
            "Bonjour tout le monde.",
            "Apprenons le russe, ",
            "l'anglais et le français !"
        )
        #line_fr_1.to_edge(LEFT, buff=0.5).to_edge(UP, buff=0.5)
        
        paragraph_phonetics_fr = Paragraph(
            "/bɔ̃ʒuʁ tu lə mɔ̃d/",
            "/a.pʁə.nɔ̃ lə ʁys/",
            "/lɑ̃.ɡlɛ e lə fʁɑ̃.sɛ/"
        )
        
        

        # Displaying text
        self.wait(1)
        self.play(
            Write(paragraph_ru)
        )
        self.wait(6)
        
        self.play(
            ReplacementTransform(
                paragraph_ru,
                paragraph_phonetics_ru
            )
        )
        self.wait(6)


        self.play(FadeOut(paragraph_phonetics_ru))
        self.wait(2)

        self.play(Write(paragraph_en))
        self.wait(6)


        self.play(
            ReplacementTransform(
                paragraph_en,
                paragraph_phonetics_en
            )
        )
        self.wait(6)

        self.play(FadeOut(paragraph_phonetics_en))
        self.wait(2)

        self.play(Write(paragraph_fr)
        )
        self.wait(6)

        self.play(
            ReplacementTransform(
                paragraph_fr,
                paragraph_phonetics_fr
            )
        )
        self.wait(6)

        

        
