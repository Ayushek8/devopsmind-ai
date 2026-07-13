from app.engine.talkops_engine import TalkOpsEngine

engine = TalkOpsEngine()

result = engine.execute(
    "List all EC2 instances"
)

print("=" * 60)
print("ENGINE RESPONSE")
print("=" * 60)

print(result)
