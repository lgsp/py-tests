from manim import *

class LawsOfPhysics(Scene):
    def construct(self):
        laws = [
            "The law of conservation of energy, which states that energy cannot be created or destroyed, only converted from one form to another.",
            "The law of conservation of momentum, which states that the total momentum of a closed system remains constant unless acted upon by an external force.",
            "The law of gravitation, which states that every object in the universe attracts every other object with a force that is directly proportional to the product of their masses and inversely proportional to the square of the distance between them.",
            "The laws of thermodynamics, which describe the relationships between heat, work, and energy.",
            "The laws of electromagnetism, which describe the ways in which electric charges and magnetic fields interact.",
            "The theory of relativity, which describes the relationship between space and time and the behavior of objects moving at high speeds.",
            "The quantum mechanics, which describes the behavior of particles on a very small scale and their interactions with energy and force."
        ]

        # REFERENCE SIZE
        # text = Text("""
        #     In general, using the interactive shell
        #     is very helpful when developing new scenes
        # """)
        for law in laws:
            law_text = Text(law)
            self.play(Write(law_text))
            self.wait(2)
        law_text.scale(0.5)
        law_text.shift(UP)
