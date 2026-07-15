import re


class LogNormalizer:

    def normalize(self, context: str):

        lines = context.splitlines()

        cleaned = []

        for line in lines:

            # Remove GitHub timestamps
            line = re.sub(
                r"^\d{4}-\d{2}-\d{2}T.*?Z\s*",
                "",
                line
            )

            # Remove GitHub group markers
            if line.startswith("##[group]"):
                continue

            if line.startswith("##[endgroup]"):
                continue

            # Remove empty lines
            if not line.strip():
                continue

            cleaned.append(line)

        return "\n".join(cleaned)