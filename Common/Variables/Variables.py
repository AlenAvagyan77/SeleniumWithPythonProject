class ProjectVariables():
    mainURL = "https://www.amazon.com"

    def get_project_root(self):
        from pathlib import Path
        return str(Path(__file__).parent.parent.parent)
