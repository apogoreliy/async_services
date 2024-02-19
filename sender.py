import requests
import json


def post_message():
    try:
        res = requests.post(
            "http://localhost:7000",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            json={
                "key": "value"
            }
        )
        res.raise_for_status()
        print(res.json())
    except Exception as e:
        print("=========== error", e)


def send():
    res = requests.get("http://localhost:7000", headers={
        "Accept": "application/json",
        "Content-Type": "application/json"
    })
    res.raise_for_status()
    print(res.json())


if __name__ == "__main__":
    post_message()
    send()
