from app.state.session_manager import SessionManager

manager = SessionManager()

manager.update(

    workflow="ci.yml",

    run_id=12345,

    branch="feature/crewai-integration",

    status="running",

    platform="github"

)

print(manager.get())