class GHCUAPIError(Exception):
    """Base class for all exceptions raised by gh_copilot_unofficial_api."""


class TokenError(GHCUAPIError):
    """Raised when an error occurs while getting the token."""


class ChatCompletionError(GHCUAPIError):
    """Raised when an error occurs while getting chat completions."""
