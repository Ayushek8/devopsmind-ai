from app.services.investigation.investigation_service import InvestigationService

service = InvestigationService()

result = service.latest_failure()

print("=" * 80)
print("FAILED RUN")
print("=" * 80)

print(result["run"])

print()

print("=" * 80)
print("FAILED JOB")
print("=" * 80)

print(result["job"]["name"])

print()

print("=" * 80)
print("FAILED STEP")
print("=" * 80)

print(result["step"])