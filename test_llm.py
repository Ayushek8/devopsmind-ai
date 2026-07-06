from app.services.llm_service import LLMService

print("=" * 50)
print("Testing Groq Connection...")
print("=" * 50)

llm = LLMService()

response = llm.ask(
    "Explain Jenkins Pipeline in one sentence."
)

print("\nAI Response:\n")
print(response)
