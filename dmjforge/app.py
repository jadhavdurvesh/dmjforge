from textual.app import App
from textual.containers import Horizontal

from dmjforge.runner import run_solution

from dmjforge.widgets.problem_panel import ProblemPanel
from dmjforge.widgets.output_panel import OutputPanel
from dmjforge.widgets.status_panel import StatusPanel


class DMJForge(App):

    CSS_PATH = "style.tcss"

    BINDINGS = [
        ("r", "run_program", "Run"),
        ("a", "add_test", "Add Test"),
        ("x", "app_quit", "Quit")
    ]

    def compose(self):

        self.output_panel = OutputPanel()
        self.status_panel = StatusPanel()

        with Horizontal():
            yield ProblemPanel()
            yield self.output_panel

        yield self.status_panel

    def action_run_program(self):

        output = run_solution(
            "workspace/two_sum/solution.py"
        )

        self.output_panel.update(
            f"[b]Output[/b]\n\n{output}"
        )

        self.status_panel.update(
            "Status\n\nProgram executed."
        )

    def action_add_test(self):

        self.status_panel.update(
            "Status\n\nAdding test case..."
        )

    def action_app_quit(self):

        self.exit()


if __name__ == "__main__":
    DMJForge().run()
