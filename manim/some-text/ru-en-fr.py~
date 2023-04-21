from manim import *

class displayText(Scene):
    def construct(self):
        # Russian
        line_ru_1 = Text('Привет всем.')
        phonetics_ru_1 = Text("[prʲɪˈvʲet vsʲɪm]")
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
        phonetics_en_1 = Text(" /hɛˈloʊ ˈɛvriˌbɑdi/")
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
        phonetics_fr_1 = Text("/bɔ̃ʒuʁ tu lə mɔ̃d")
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
        self.wait(3)
        
        self.play(ReplacementTransform(line_ru_1, phonetics_ru_1))
        self.play(ReplacementTransform(line_ru_2, phonetics_ru_2))
        self.play(ReplacementTransform(line_ru_3, phonetics_ru_3))
        self.wait(3)


        self.play(ReplacementTransform(phonetics_ru_1, line_en_1))
        self.play(ReplacementTransform(phonetics_ru_2, line_en_2))
        self.play(ReplacementTransform(phonetics_ru_3, line_en_3))
        self.wait(3)


        self.play(ReplacementTransform(line_en_1, phonetics_en_1))
        self.play(ReplacementTransform(line_en_2, phonetics_en_2))
        self.play(ReplacementTransform(line_en_3, phonetics_en_3))
        self.wait(3)

        self.play(ReplacementTransform(phonetics_en_1, line_fr_1))
        self.play(ReplacementTransform(phonetics_en_2, line_fr_2))
        self.play(ReplacementTransform(phonetics_en_3, line_fr_3))
        self.wait(3)

        self.play(ReplacementTransform(line_fr_1, phonetics_fr_1))
        self.play(ReplacementTransform(line_fr_2, phonetics_fr_2))
        self.play(ReplacementTransform(line_fr_3, phonetics_fr_3))
        self.wait(3)

        

