import requests

while True:
    q = input("You: ")

    r = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"message": q}
    )

    print("Bot:", r.json()["answer"])