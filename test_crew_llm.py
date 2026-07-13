from app.crew.config.llm import llm

response = llm.call(
    "Reply with only: CrewAI is successfully connected to Groq."
)

print(response)
