import re


class ContextExtractor:

    KEYWORDS = [

        "error",

        "exception",

        "traceback",

        "failed",

        "panic",

        "fatal",

        "permission denied",

        "no module",

        "cannot",

        "not found",

        "timeout",

        "denied",

        "crash",

        "oom",

        "segmentation fault"

    ]

    WINDOW = 20

    def extract(self, logs):

        contexts = []

        for filename, content in logs.items():

            lines = content.splitlines()

            for index, line in enumerate(lines):

                lower = line.lower()

                if any(

                    keyword in lower

                    for keyword in self.KEYWORDS

                ):

                    start = max(

                        0,

                        index - self.WINDOW

                    )

                    end = min(

                        len(lines),

                        index + self.WINDOW

                    )

                    context = "\n".join(

                        lines[start:end]

                    )

                    contexts.append(

                        {

                            "file": filename,

                            "keyword": line,

                            "context": context

                        }

                    )

        return contexts