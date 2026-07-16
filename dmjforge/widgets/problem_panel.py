import os
from textual.widgets import Static

class ProblemPanel(Static):

    def __init__(self):
        workspace = "workspace"

        if os.path.exists(workspace):
            folders = sorted(
                f for f in os.listdir(workspace)
                if os.path.isdir(os.path.join(workspace, f))
            )
        else:
            folders = []

        content = "[b]Problems[/b]\n\n"

        for folder in folders:
            content += f"• {folder}\n"

        super().__init__(content)
