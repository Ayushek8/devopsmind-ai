import re


class ErrorParser:

    ERROR_PATTERNS = [

        r"ModuleNotFoundError:.*",

        r"ImportError:.*",

        r"JSONDecodeError:.*",

        r"TypeError:.*",

        r"ValueError:.*",

        r"AttributeError:.*",

        r"AssertionError.*",

        r"RuntimeError:.*",

        r"PermissionError:.*",

        r"KeyError:.*",

        r"NameError:.*",

        r"FileNotFoundError:.*",

        r"Exception:.*",

        r"panic:.*",

        r"FAILED.*"

    ]

    def extract(self, logs):

        findings = []

        for filename, content in logs.items():

            # Ignore workflow summary logs
            if filename.startswith("0_"):
                continue

            lines = content.splitlines()

            for index, line in enumerate(lines):

                for pattern in self.ERROR_PATTERNS:

                    if re.search(pattern, line):

                        findings.append({

                            "file": filename,

                            "error": line,

                            "context": "\n".join(

                                lines[max(0, index-8):index+12]

                            )

                        })

        return findings