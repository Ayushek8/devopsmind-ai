from app.tools.git.git_tool import GitTool


class JenkinsTool:

    def __init__(self):
        self.git = GitTool()

    def load_pipeline(self, path: str):

        return self.git.read_file(path)