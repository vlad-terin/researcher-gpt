import requests

print(
        requests.post(
            "https://gpt-researcher-9jgl.onrender.com",
            json={
                "query": "what is the weather in sydney?"
                }
            ).json()
    )
