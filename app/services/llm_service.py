from groq import Groq

from app.core.config import settings


class LLMService:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def ask(self, prompt: str):

        response = self.client.chat.completions.create(

            model="openai/gpt-oss-120b",

            temperature=0,

            response_format={
                "type": "json_object"
            },

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response.choices[0].message.content