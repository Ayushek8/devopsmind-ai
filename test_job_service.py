from app.services.github.jobs.job_service import JobService

service = JobService()

run = input("Run ID : ")

job = service.failed(

    int(run)

)

print(job)