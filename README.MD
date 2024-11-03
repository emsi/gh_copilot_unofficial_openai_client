# GitHub Copilot Unoffician OpenAI API Client

This project is a Python library that enables you to use GitHub Copilot models through OpenAI's API interface. By providing a GitHub token (gho_), you can access various AI models including GPT-4, Claude, and others while only paying GitHub Copilot's fixed subscription fee rather than OpenAI's per-token pricing.

## Key features:
- Uses standard OpenAI Python library interface
- Supports multiple AI models including Claude-3.5-sonnet
- Fixed pricing through GitHub Copilot subscription

## Requirements

A github's access token (`gho_...`) is required. To obtain it, follow this procedure:
https://github.com/VSCodium/vscodium/discussions/1487 

## Example

```
>>> from gh_copilot_unofficial_api import openai
... client = openai.CopilotOpenAI().client("gho_...")

>>> type(client)
<class 'openai.OpenAI'>

>>> models = client.models.list()
...
... for m in models.to_dict()["data"]: print(m["id"])
...
gpt-3.5-turbo
gpt-3.5-turbo-0613
gpt-4
gpt-4-0613
gpt-4o
gpt-4o-2024-05-13
gpt-4-o-preview
gpt-4o-2024-08-06
o1-preview
o1-preview-2024-09-12
o1-mini
o1-mini-2024-09-12
text-embedding-ada-002
text-embedding-3-small
text-embedding-3-small-inference
gpt-4o-mini
gpt-4o-mini-2024-07-18
gpt-4-0125-preview
claude-3.5-sonnet

>>> chat_completion = client.chat.completions.create(
... messages=[
...     {
...         "role": "user",
...         "content": "Who are you?",
...     }
... ],
... model="claude-3.5-sonnet",
... )
...
chat_completion.choices[0].message
ChatCompletionMessage(content="I'm Claude, an AI assistant created by Anthropic. I aim to be direct and honest in my interactions while being genuinely helpful. I'm capable of engaging on a wide range of topics but prefer to be upfront about my capabilities and limitations.", refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None)
```