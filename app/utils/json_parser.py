import json
import re


class JSONParser:

    @staticmethod
    def parse(text: str):

        text = text.strip()

        # Remove ```json
        text = re.sub(
            r"^```json",
            "",
            text,
            flags=re.IGNORECASE
        )

        # Remove opening ```
        text = re.sub(
            r"^```",
            "",
            text
        )

        # Remove closing ```
        text = re.sub(
            r"```$",
            "",
            text
        )

        text = text.strip()

        return json.loads(text)
