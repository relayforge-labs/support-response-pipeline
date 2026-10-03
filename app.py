"""Run the gateway example with environment configuration."""
import json
import os
from urllib.request import Request, urlopen

payload = {"model": os.getenv("OPENAI_MODEL", "chat-default"), "messages": [{"role": "user", "content": "Summarize the supplied operations note."}], "max_tokens": 300}
request = Request(os.environ["OPENAI_BASE_URL"].rstrip("/") + "/chat/completions", json.dumps(payload).encode(), {"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"], "Content-Type": "application/json"})
with urlopen(request, timeout=45) as response:
    print(json.load(response)["choices"][0]["message"]["content"])
