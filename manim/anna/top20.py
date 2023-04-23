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

def disp_full_part_full(self, full, part, images, lang):
    self.play(Write(full, run_time = 5))
    self.wait(5)
    self.play(FadeOut(full))

    for img in images:
        pic = ImageMobject(img)
        self.add(pic)
        self.wait(3)
        self.remove(pic)
        
    self.play(Write(part, run_time = 5))
    self.wait(5)
        
    self.play(ReplacementTransform(part, full), run_time=5)
    self.wait(5)
    self.play(FadeOut(full))
    last_pic = ImageMobject(images[-1])
    self.add(last_pic)
    self.wait(4)
    self.remove(last_pic)

    if lang.lower() == "en":
        written, phon = "Subscribe", "/səbˈskraɪb/"
    elif lang.lower() == "fr":
        written, phon = "Abonnez-vous", "/abɔne vu/"
    elif lang.lower() == "ru":
        written, phon = "Подпишитесь", "/pɐd'piʂitʲɪsʲ/"
    sub = Paragraph(written, phon)
    self.play(GrowFromCenter(sub))
    self.wait(5)
    youtube_png = ImageMobject("youtube_logo.png")
    self.add(youtube_png)
    self.wait()

# English    
class One(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        one = Paragraph(
            "Subject: The cat ",
            "Subject: /Də kæt/ ",
            "Verb:    is sleeping ",
            "Verb:    /ɪz ˈslipɪŋ/",
            "Object:  on the mat.",
            "Object:  /ɑn ðə mæt/"
        )

        
        full_one = Paragraph(
            "The cat is sleeping on the mat.",
            "/Də kæt ɪz ˈslipɪŋ ɑn ðə mæt/"
        )

        svo = [
            "cat.jpeg",
            "sleeping.jpeg",
            "mat.jpeg",
            "the_cat_is_sleeping_on_the_mat.jpeg"
        ]
        disp_full_part_full(
            self,
            full=full_one,
            part=one,
            images=svo,
            lang="en"
        )


# French
class Un(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        un = Paragraph(
            "Sujet : Le chat ",
            "Subjet : /lə ʃa/ ",
            "Verbe :    dort ",
            "Verbe :    /dɔʁ/",
            "Objet :  sur le tapis.",
            "Objet :  /syʁ lə tapi/"
        )

        
        full_un = Paragraph(
            "Le chat dort sur le tapis.",
            "/lə ʃa dɔʁ syʁ lə tapi/"
        )

        svo = [
            "cat.jpeg",
            "sleeping.jpeg",
            "mat.jpeg",
            "the_cat_is_sleeping_on_the_mat.jpeg"
        ]
        disp_full_part_full(
            self,
            full=full_un,
            part=un,
            images=svo,
            lang="fr"
        )
        


# Russian
class Odin(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        odin = Paragraph(
            "Предмет: Кошка",
            "Предмет: /kɐʂˈka/",
            "Глагол:  спит",
            "Глагол:    /spʲit/",
            "Дополнение:  на ковре.",
            "Дополнение:  /nɐ ˈkovrʲɪ/"
        )

        
        full_odin = Paragraph(
            "Кошка спит на ковре.",
            "/kɐʂˈka spʲit nɐ ˈkovrʲɪ/"
        )

        svo = [
            "cat.jpeg",
            "sleeping.jpeg",
            "mat.jpeg",
            "the_cat_is_sleeping_on_the_mat.jpeg"
        ]
        disp_full_part_full(
            self,
            full=full_odin,
            part=odin,
            images=svo,
            lang="ru"
        )
        
        


class Two(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        # English 
        two = Paragraph( 
            "Subject: I ",
            "Subject: /ai/ ",            
            "Verb:    like ",
            "Verb:    /laɪk/",            
            "Object:  apples and bananas.",
            "Object:  /ˈæplz ənd bəˈnænəz/"
        )

        full_two = Paragraph(
            "I like apples and bananas.",
            "/ai laɪk ˈæplz ənd bəˈnænəz/"
        )
        
        
        disp_full_part_full(self, full=full_two, part=two)


class Three(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        # English 
        three = Paragraph( 
            "Subject: She ",
            "Subject: /ʃi/ ",            
            "Verb:    bought ",
            "Verb:    /bɔt/",            
            "Object:  a book at the store.",
            "Object:  /ə bʊk æt ðə stɔr/"
        )

        full_three = Paragraph(
            "She bought a book at the store.",
            "/ʃi bɔt ə bʊk æt ðə stɔr/"
        )
        
        
        disp_full_part_full(self, full=full_three, part=three)


class Four(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        # English 
        four = Paragraph( 
            "Subject: I ",
            "Subject: /ai/ ",            
            "Verb:    need to finish",
            "Verb:    /nid tu ˈfɪnɪʃ/",            
            "Object:  my homework.",
            "Object:  /mai ˈhoʊmˌwɜrk//"
        )

        full_four = Paragraph(
            "I need to finish my homework.",
            "/ai nid tu ˈfɪnɪʃ mai ˈhoʊmˌwɜrk/"
        )
        
        
        disp_full_part_full(self, full=full_four, part=four)

        
class Five(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        # English 
        five = Paragraph( 
            "Subject: The flowers ",
            "Subject: /ðə ˈflaʊərz/ ",            
            "Verb:    are",
            "Verb:    /ɑr/",            
            "Object:  in the vase.",
            "Object:  /ɪn ðə veɪs/"
        )

        full_five = Paragraph(
            "The flowers are in the vase.",
            "/ðə ˈflaʊərz ɑr ɪn ðə veɪs/"
        )
        
        
        disp_full_part_full(self, full=full_five, part=five)
        
        
        six_to_ten = Paragraph(
            "6) The car that I saw was red.",
            "7) It is raining outside.",
            "8) The top of the mountain is covered in snow.",
            "9) I made a sandwich for lunch.",
            "10) She writes with a pen."
        )

        eleven_to_fifteen = Paragraph(
            "11) He works as a doctor.",
            "12) The book is on the table.",
            "13) I want to be a firefighter when I grow up.",
            "14) The picture was painted by my sister.",
            "15) I do not like spiders. "
        )

        sixteen_to_twenty = Paragraph(
            "16) He is my best friend.",
            "17) I love to read books.",
            "18) This is my favorite toy.",
            "19) The flowers are beautiful.",
            "20) Do you want the red or the blue one?"
        )
        

        
