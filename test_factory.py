from app.platforms.factory.platform_factory import PlatformFactory

factory = PlatformFactory()

github = factory.get("github")

print(type(github))

print()

print(github.list_workflows())