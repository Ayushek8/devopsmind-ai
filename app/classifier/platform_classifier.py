class PlatformClassifier:

    @staticmethod
    def detect(text: str):

        text = text.lower()

        # -----------------------------
        # GitHub
        # -----------------------------

        if any(keyword in text for keyword in [

            "github",
            "workflow",
            "github actions",
            "deploy latest",
            "deploy code",
            "deploy latest code",
            "pull request",
            "merge request"

        ]):

            return "github"

        # -----------------------------
        # Jenkins
        # -----------------------------

        if any(keyword in text for keyword in [

            "jenkins",
            "job",
            "build job",
            "trigger build",
            "pipeline"

        ]):

            return "jenkins"

        # -----------------------------
        # AWS
        # -----------------------------

        if any(keyword in text for keyword in [

            "ec2",
            "s3",
            "iam",
            "vpc",
            "route53",
            "alb",
            "cloudfront",
            "lambda",
            "rds"

        ]):

            return "aws"

        # -----------------------------
        # Kubernetes
        # -----------------------------

        if any(keyword in text for keyword in [

            "kubernetes",
            "kubectl",
            "pod",
            "deployment",
            "namespace",
            "service"

        ]):

            return "kubernetes"

        # -----------------------------
        # Terraform
        # -----------------------------

        if any(keyword in text for keyword in [

            "terraform",
            ".tf",
            "terraform plan",
            "terraform apply"

        ]):

            return "terraform"

        return "general"