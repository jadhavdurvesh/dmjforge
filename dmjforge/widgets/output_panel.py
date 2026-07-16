from textual.widgets import Static

class OutputPanel(Static):

    def __init__(self):
        super().__init__(
            "[b]Output[/b]\n\nPress R to run."
        )
