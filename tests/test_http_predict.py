import pytest
import requests


@pytest.mark.xfail(reason="Stub test")
def test_http_endpoint():
    api_url = "http://localhost:8080/api/v1/flan-t5-small-caikit/task/text-generation"

    json_input = {
        "inputs": "At what temperature does liquid Nitrogen boil?",
        "parameters": {"max_new_tokens": 200, "min_new_tokens": 10},
    }
    response = requests.post(
        api_url,
        json=json_input,
    )
    assert response.status_code == 200
