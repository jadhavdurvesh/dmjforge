from textual.widgets import Static

class FilePanel(Static):

    def __init__(self):
        super().__init__(
            "[b]Files[/b]\n\n"
            "No problem selected."
        )
