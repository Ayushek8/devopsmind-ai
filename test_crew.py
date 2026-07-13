from app.crew.crews.talkops_crew import TalkOpsCrew

crew = TalkOpsCrew()

result = crew.run(
    "List all EC2 instances"
)

print("=" * 80)
print(result)
