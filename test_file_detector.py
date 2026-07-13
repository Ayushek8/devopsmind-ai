from app.reviewers.file_detector import FileDetector

content = """
pipeline {
    agent any

    stages {
        stage("Build") {
            steps {
                sh "mvn clean package"
            }
        }
    }
}
"""

detector = FileDetector()

print("=" * 60)
print("Detected File Type")
print("=" * 60)

print(detector.detect(content))
