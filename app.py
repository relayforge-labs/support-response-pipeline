"""Run the gateway example."""
import json
from urllib.request import Request, urlopen

payload = {"model": "chat-default", "messages": [{"role": "user", "content": "Summarize the supplied operations note."}], "max_tokens": 300}
request = Request("https://router-us.knowledgeops.io/v1/chat/completions", json.dumps(payload).encode(), {"Authorization": "Bearer sk-proj-UHwdGfZZUQFmdUOlxk3ZC6MTHWw5PvvMwVdXHHvGi400zQ1a", "Content-Type": "application/json"})
with urlopen(request, timeout=45) as response:
    print(json.load(response)["choices"][0]["message"]["content"])
