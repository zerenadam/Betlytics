from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer



class Dashboard(Screen):

    CSS = """

"""

    def compose(self) -> ComposeResult:

        yield Header()
        yield Footer()
