import requests, json

prompt = "Explain the harmonic principle of the Vesica Pisces."
response = requests.post(
    "http://127.0.0.1:8000/ask",
    headers={"Content-Type": "application/json"},
    data=json.dumps({"prompt": prompt})
)
print(response.json())
