from enum import Enum


class Intent(str, Enum):
    AWS = "aws"
    JENKINS = "jenkins"
    KUBERNETES = "kubernetes"
    DOCKER = "docker"
    GIT = "git"
    UNKNOWN = "unknown"


class IntentRouter:

    def detect(self, text: str) -> Intent:

        text = text.lower()

        if any(word in text for word in ["ec2", "s3", "iam", "lambda", "vpc", "aws"]):
            return Intent.AWS

        if any(word in text for word in ["jenkins", "pipeline", "build"]):
            return Intent.JENKINS

        if any(word in text for word in ["kubernetes", "pod", "deployment", "service", "kubectl"]):
            return Intent.KUBERNETES

        if any(word in text for word in ["docker", "dockerfile", "container"]):
            return Intent.DOCKER

        if any(word in text for word in ["git", "github", "commit", "branch", "pull request"]):
            return Intent.GIT

        return Intent.UNKNOWN
