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


def disp_full_part_full(self, full, part, images, lang, full_scale=1):
    self.play(Write(full.scale(full_scale), run_time = 5))
    self.wait(5)
    self.play(FadeOut(full))

    for img in images:
        pic = ImageMobject(img)
        self.add(pic.scale(0.25))
        self.wait(3)
        self.remove(pic)
        
    self.play(Write(part.scale(full_scale), run_time = 5))
    self.wait(5)
        
    self.play(ReplacementTransform(part, full), run_time=5)
    self.wait(5)
    self.play(FadeOut(full))
    

    if lang.lower() == "en":
        written, phon = "Subscribe", "/səbˈskraɪb/"
    elif lang.lower() == "fr":
        written, phon = "Abonnez-vous", "/abɔne vu/"
    elif lang.lower() == "ru":
        written, phon = "Подпишитесь", "/pɐd'piʂitʲɪsʲ/"
    sub = Paragraph(written, phon)
    self.play(GrowFromCenter(sub))
    self.wait(3)
    youtube_png = ImageMobject("youtube_logo.png")
    self.add(youtube_png.scale(0.85))
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
        title = Title(f"YouTube Shorts With Manim {manim.__version__}")
        self.add(title)
        youtube_shorts = SVGMobject(
            "youtube_shorts_icon.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.25)
        self.play(FadeIn(youtube_shorts.to_edge(2.5*UP)))
        
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
        
        

# English 
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
        title = Title(f"YouTube Shorts With Manim {manim.__version__}")
        self.add(title)
        youtube_shorts = SVGMobject(
            "youtube_shorts_icon.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.5)
        self.add(youtube_shorts.to_edge(2.5*DOWN))
        
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

        svo = [
            "apples.jpeg",
            "bananas.jpeg"
        ]
        
        disp_full_part_full(
            self,
            full=full_two,
            part=two,
            images=svo,
            lang="en"
        )

# French
class Deux(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title(f"YouTube Shorts avec Manim {manim.__version__}")
        self.add(title)
        youtube_shorts = SVGMobject(
            "youtube_shorts_icon.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.5)
        self.add(youtube_shorts.to_edge(2.5*DOWN))
        
        deux = Paragraph( 
            "Sujet : J' (Je) ",
            "Sujet : /ʒ/ ",            
            "Verbe : aime ",
            "Verbe : /ɛm/",            
            "Objet : les pommes et les bananes.",
            "Objet :  /le pɔm e le banan/"
        )

        full_deux = Paragraph(
            "J'aime les pommes et les bananes.",
            "/ʒɛm le pɔm e le banan/"
        )

        svo = [
            "apples.jpeg",
            "bananas.jpeg"
        ]
        
        disp_full_part_full(
            self,
            full=full_deux,
            part=deux,
            images=svo,
            lang="fr"
        )


# Russian
class Dva(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        #titre = MarkupText( "Ютуб Шорты с Маним ")
        titre = "YouTube Shorts With Manim "
        titre += f"{manim.__version__}"
        title = Title(titre)
        self.add(title)
        youtube_shorts = SVGMobject(
            "youtube_shorts_icon.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.5)
        self.add(youtube_shorts.to_edge(2.5*DOWN))
        
        dva = Paragraph( 
            "Предмет : Я",
            "Предмет : /ja/ ",            
            "Глагол : люблю",
            "Глагол : /ljublʲu/",            
            "Дополнение : яблоки и бананы.",
            "Дополнение :  /jablɐkʲɪ i bɐnanɨ/"
        )

        full_dva = Paragraph(
            "Я люблю яблоки и бананы.",
            "/ja ljublʲu jablɐkʲɪ i bɐnanɨ/"
        )

        svo = [
            "apples.jpeg",
            "bananas.jpeg"
        ]
        
        disp_full_part_full(
            self,
            full=full_dva,
            part=dva,
            images=svo,
            lang="ru"
        )
        
# English
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
        title = Title("Learn English With Manim \#3")
        self.add(title)
        youtube_shorts = SVGMobject(
            "youtube_shorts_icon.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.5)
        self.add(youtube_shorts.to_edge(2.5*DOWN))
        
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

        svo = [
            "girl.jpeg",
            "buy.jpeg",
            "book.jpeg",
            "she_is_reading_a_book.jpeg"
        ]
        
        disp_full_part_full(
            self,
            full=full_three,
            part=three,
            images=svo,
            lang="en"
        )


# French
class Trois(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Apprenez le Français avec Manim épisode 3")
        self.add(title.scale(0.75))
        youtube_shorts = SVGMobject(
            "youtube_shorts_icon.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.5)
        self.add(youtube_shorts.to_edge(2.5*DOWN))
        
        trois = Paragraph( 
            "Sujet : Elle ",
            "Sujet : /ɛl/ ",            
            "Verbe : a acheté",
            "Verbe : /a aʃəte/",            
            "Objet : un livre au magasin.",
            "Objet :  /œ̃ livʁ o maɡazɛ̃/"
        )

        full_trois = Paragraph(
            "Elle a acheté un livre au magasin.",
            "/ɛl a aʃəte œ̃ livʁ o maɡazɛ̃/"
        )

        svo = [
            "girl.jpeg",
            "buy.jpeg",
            "book.jpeg",
            "she_is_reading_a_book.jpeg"
        ]
        
        disp_full_part_full(
            self,
            full=full_trois,
            part=trois,
            images=svo,
            lang="fr",
            full_scale=0.75
        )


# Russian
class Tri(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Learn Russian With Manim \#3")
        self.add(title.scale(0.75))
        youtube_shorts = SVGMobject(
            "youtube_shorts_icon.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.5)
        self.add(youtube_shorts.to_edge(2.5*DOWN))
        
        tri = Paragraph( 
            "Предмет : Она",
            "Предмет : /ɐˈna/ ",            
            "Глагол : купила",
            "Глагол : /kupʲɪˈla/",            
            "Дополнение : книгу в магазине.",
            "Дополнение :  /ˈknʲɪɡʊ f məɡɐˈzinʲɪ/"
        )

        full_tri = Paragraph(
            "Она купила книгу в магазине.",
            "/ɐˈna kupʲɪˈla ˈknʲɪɡʊ f məɡɐˈzinʲɪ/"
        )

        svo = [
            "girl.jpeg",
            "buy.jpeg",
            "book.jpeg",
            "she_is_reading_a_book.jpeg"
        ]
        
        disp_full_part_full(
            self,
            full=full_tri,
            part=tri,
            images=svo,
            lang="ru",
            full_scale=0.75
        )
        
# English
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
        title = Title("Learn English With Manim \#4")
        self.add(title)
        youtube_shorts = SVGMobject(
            "youtube_shorts_icon.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.5)
        self.add(youtube_shorts.to_edge(2.5*DOWN))
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
        
        svo = [
            "need.jpeg",
            "finish.jpeg",
            "homework.jpeg",
            "I-need-to-finish-my-homework.jpeg"
        ]
        
        disp_full_part_full(
            self,
            full=full_four,
            part=four,
            images=svo,
            lang="en",
            full_scale=0.85
        )

# French
class Quatre(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Apprenez le Français avec Manim \#4")
        self.add(title)
        youtube_shorts = SVGMobject(
            "youtube_shorts_icon.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.5)
        self.add(youtube_shorts.to_edge(2.5*DOWN))
        quatre = Paragraph( 
            "Sujet : Je ",
            "Sujet : /ʒə/ ",            
            "Verbe : dois finir ",
            "Verbe : /dwɑ finiʁ/",            
            "Objet : mes devoirs.",
            "Objet : /me dəvwaʁ/"
        )

        full_quatre = Paragraph(
            "Je dois finir mes devoirs.",
            "/ʒə dwɑ finiʁ me dəvwaʁ/"
        )
        
        svo = [
            "need.jpeg",
            "finish.jpeg",
            "homework.jpeg",
            "I-need-to-finish-my-homework.jpeg"
        ]
        
        disp_full_part_full(
            self,
            full=full_quatre,
            part=quatre,
            images=svo,
            lang="fr",
            full_scale=0.85
        )        

# Russian
class Tchet(Scene):
    def setup(self, add_border=True):
        if add_border:
            self.border = Rectangle(
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
                color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        title = Title("Learn Russian With Manim \#4")
        self.add(title)
        youtube_shorts = SVGMobject(
            "youtube_shorts_icon.svg",
            fill_opacity=1,
            fill_color=RED
        ).scale(0.5)
        self.add(youtube_shorts.to_edge(2.5*DOWN))
        tchet = Paragraph( 
            "Предмет : Мне ",
            "Предмет: : /mnʲe/ ",            
            "Глагол : нужно закончить ",
            "Глагол : /nuˈʐno zəkɐnˈt͡ɕitʲ/",            
            "Дополнение : мою домашнюю работу.",
            "Дополнение : /məˈju dəmɐˈʂnʲʊjʊ rɐˈbotʊ/"
        )

        full_tchet = Paragraph(
            "Мне нужно закончить ",
            "/mnʲe nuˈʐno zəkɐnˈt͡ɕitʲ/",
            "мою домашнюю работу.",
            "/məˈju dəmɐˈʂnʲʊjʊ rɐˈbotʊ/"
        )
        
        svo = [
            "need.jpeg",
            "finish.jpeg",
            "homework.jpeg",
            "I-need-to-finish-my-homework.jpeg"
        ]
        
        disp_full_part_full(
            self,
            full=full_tchet,
            part=tchet,
            images=svo,
            lang="ru",
            full_scale=0.65
        )

        
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
        

        
