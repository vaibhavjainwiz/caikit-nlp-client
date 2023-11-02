import requests


api_url = "http://localhost:8080/api/v1/flan-t5-small-caikit/task/text-generation"

json_input = {
    "inputs": "At what temperature does liquid Nitrogen boil?",
    "parameters": {"max_new_tokens": 200, "min_new_tokens": 10},
}
response = requests.post(
    api_url,
    json=json_input,
)
print("response", response)
