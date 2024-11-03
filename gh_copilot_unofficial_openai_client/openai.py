import requests
from openai import OpenAI

from .errors import TokenError


class CopilotOpenAI:
    """
    Unofficial GitHub Copilot API client implementation
    """

    API_BASE = "https://api.githubcopilot.com"
    GITHUB_API_BASE = "https://api.github.com"

    editor_version = "vscode/1.93.1"
    editor_plugin_version = "copilot/1.234.1127"
    user_agent = "GithubCopilot/1.234.1127"
    copilot_language_server_version = "1.234.1127"

    @classmethod
    def _headers(cls):
        return {
            "editor-version": cls.editor_version,
            "editor-plugin-version": cls.editor_plugin_version,
            "user-agent": cls.user_agent,
            "copilot-language-server-version": cls.copilot_language_server_version,
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
