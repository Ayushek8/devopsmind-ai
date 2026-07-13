from pathlib import Path


class GitTool:

    def read_file(self, path: str):

        file = Path(path)

        if not file.exists():
            raise FileNotFoundError(path)

        return file.read_text()