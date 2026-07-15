from app.platforms.github.github_platform import GitHubPlatform


class PlatformFactory:

    def __init__(self):

        self.platforms = {

            "github": GitHubPlatform(),

        }

    def get(

        self,

        platform_name

    ):

        platform = self.platforms.get(

            platform_name

        )

        if platform is None:

            raise Exception(

                f"Unsupported Platform : {platform_name}"

            )

        return platform