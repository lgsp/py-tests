"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc
from .results import results

question_style = {
    "bg": "white",
    "padding": "2em",
    "border_radius": "25px",
    "w": "100%",
    "align_items": "left",
}


class State(pc.State):
    """The app state."""

    answers = [
        "A", "None",
        [True, False, False, True, False],
        [False, False, False, True, True]
    ]
    answer_key = [
        "A", "[1, 2, 3, 4]",
        [True, False, False, True, False],
        [False, False, False, True, True]
    ]
    score: int

    def set_answers(self, answer, index, sub_index=None):
        if sub_index is None:
            self.answers[index] = answer
        else:
            self.answers[index][sub_index] = answer

    def submit(self):
        total, correct = 0, 0
        for i in range(len(self.answers)):
            if self.answers[i] == self.answer_key[i]:
                correct += 1
            else:
                print(self.answers[i], self.answer_key[i])
            total += 1

        self.score = int(correct / total * 100)
        return pc.redirect("/result")


def header():
    exemple = "Voici un exemple de questionnaire fait avec Pynecone."
    result_exp = "Une fois soumises, les reponses seront affichees sur la "
    result_exp += "page des resultats."
    return pc.vstack(
        pc.heading("Faisons un petit test"),
        pc.divider(),
        pc.text(exemple),
        pc.text(result_exp),
        style=question_style,
    )


def question1():
    """The main view."""
    return pc.vstack(
        pc.heading("Question 1"),
        pc.text(
            "Quel est le nombre le plus grand A = 2",
            pc.text("6", as_="sup"),
            " ou B = 6",
            pc.text("2", as_="sup"),
            " ?"
        ),
        pc.divider(),
        pc.radio_group(
            ["A", "B"], on_change=lambda answer: State.set_answers(answer, 0)
        ),
        style=question_style,
    )


def question2():
    q2 = "En Python quel sera la sortie de l'operateur (+) "
    q2 += "dans le bloc de code suivant ?"
    return pc.vstack(
        pc.heading("Question 2"),
        pc.text(q2),
        pc.code_block(
            """a = [1, 2]
b = a
b += [3, 4]
print(a)""",
            language="python",
        ),
        pc.radio_group(
            ["[1, 2, 3, 4]", "[1, 2]"],
            on_change=lambda answer: State.set_answers(answer, 1),
        ),
        style=question_style,
    )


def question3():
    q3 = "Quelles sont les expressions qui correspondent "
    q3 += "a une parabole passant coupant l'axe des abscisses "
    q3 += "en -5 et 1 avec un maximum ?"
    return pc.vstack(
        pc.heading("Question 3"),
        pc.text(q3),
        pc.vstack(
            pc.checkbox(
                pc.text("9 - (x + 2)",
                        pc.text("2", as_="sup"),
                ),
                on_change=lambda answer: State.set_answers(answer, 2, 0),
            ),
            pc.checkbox(
                pc.text("(x + 2)",
                        pc.text("2", as_="sup"),
                        " - 9"
                ),
                on_change=lambda answer: State.set_answers(answer, 2, 1),
            ),
            pc.checkbox(
                pc.text("x",
                        pc.text("2", as_="sup"),
                        " + 4x - 5"
                ),
                on_change=lambda answer: State.set_answers(answer, 2, 2),
            ),
            pc.checkbox(
                pc.text("-x",
                        pc.text("2", as_="sup"),
                        " - 4x + 5"
                ),
                on_change=lambda answer: State.set_answers(answer, 2, 3),
            ),
            pc.checkbox(
                pc.text("(x - 1)(x + 5)"),
                on_change=lambda answer: State.set_answers(answer, 2, 4),
            ),
            align_items="left",
        ),
        style=question_style,
    )


def question4():
    q4 = """Considerer un de truque tel que la probabilite d'obtenir une face
    soit proportionnelle a cette face. Par exemple il est 2 fois plus probable
    d'obtenir 2 que 1. Quelle est la probabilite d'obtenir 1 ?"""
    return pc.vstack(
        pc.heading("Question 4"),
        pc.text(q4),
        pc.vstack(
            pc.checkbox(
                pc.text("1/6"),
                on_change=lambda answer: State.set_answers(answer, 3, 0),
            ),
            pc.checkbox(
                pc.text("1/12"),
                on_change=lambda answer: State.set_answers(answer, 3, 1),
            ),
            pc.checkbox(
                pc.text("1/24"),
                on_change=lambda answer: State.set_answers(answer, 3, 2),
            ),
            pc.checkbox(
                pc.text("1/21"),
                on_change=lambda answer: State.set_answers(answer, 3, 3),
            ),
            pc.checkbox(
                pc.text("2/42"),
                on_change=lambda answer: State.set_answers(answer, 3, 4),
            ),
            align_items="left",
        ),
        style=question_style,
    )


def index():
    """The main view."""
    return pc.center(
        pc.vstack(
            header(),
            question1(),
            question2(),
            question3(),
            question4(),
            pc.button(
                "Submit",
                bg="black",
                color="white",
                width="6em",
                padding="1em",
                on_click=State.submit,
            ),
            spacing="1em",
        ),
        padding_y="2em",
        height="100vh",
        align_items="top",
        bg="#ededed",
        overflow="auto",
    )


def result():
    return results(State)


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, title="Pynecone Quiz")
app.add_page(result, title="Quiz Results")
app.compile()
