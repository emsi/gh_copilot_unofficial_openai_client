import requests
from openai import OpenAI

from .errors import TokenError


class CopilotOpenAI:
    """
    Unofficial GitHub Copilot API client implementation
    """

    API_BASE = "https://api.githubcopilot.com"
    GITHUB_API_BASE = "https://api.github.com"

    editor_version = "vscode/1.95.1"
    editor_plugin_version = "copilot-chat/0.22.1"
    user_agent = "GitHubCopilotChat/0.22.1"

    @classmethod
    def _headers(cls):
        return {
            "editor-version": cls.editor_version,
            "editor-plugin-version": cls.editor_plugin_version,
            "user-agent": cls.user_agent,
        }

    @classmethod
    def _token(cls, gho_token: str):
        url = f"{cls.GITHUB_API_BASE}/copilot_internal/v2/token"
        headers = {
            "authorization": f"token {gho_token}",
            **cls._headers(),
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            try:
                message = response.json()["message"]
            except Exception:
                message = response.text
            raise TokenError(response, message)

        token_response = response.json()

        return token_response["token"]

    @classmethod
    def client(cls, gho_token: str, **kwargs):
        """Instantiate OpenAI client for GitHub Copilot"""
        client = OpenAI(
            api_key=cls._token(gho_token),
            base_url=cls.API_BASE,
            default_headers=cls._headers(),
            **kwargs,
        )
        return client
