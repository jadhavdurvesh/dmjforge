from textual.app import App
from textual.widgets import Header, Footer, Static

class DMJForge(App):
    def compose(self):
        yield Header()
        yield Static("Welcome to DMJForge v0.1")
        yield Footer()