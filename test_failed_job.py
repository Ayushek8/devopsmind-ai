from app.github.log_downloader import LogDownloader

downloader = LogDownloader()

run_id = int(input("Run ID : "))

job = downloader.failed_job(run_id)

print("=" * 80)
print("RESULT")
print("=" * 80)

print(job)