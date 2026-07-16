from textual.widgets import Static

class StatusPanel(Static):
    def __init__(self):
        super().__init__(
            "[b]Status[/b]\n\nReady"
        )
