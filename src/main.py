from textual.app import App
from pages.dashboard import Dashboard



class Betlytics(App):

    def on_mount(self):

        self.theme = 'monokai'
        self.push_screen(Dashboard())


Betlytics().run()