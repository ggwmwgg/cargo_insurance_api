import requests
from datetime import datetime
from main import app
from fastapi.testclient import TestClient

# For load rates
url = "http://localhost:8000/load_rates"
rates = {
  "2020-06-01": [
    {
      "cargo_type": "Glass",
      "rate": "0.04"
    },
    {
      "cargo_type": "Other",
      "rate": "0.04"
    }
  ],
  "2020-07-01": [
    {
      "cargo_type": "Glass",
      "rate": "0.035"
    },
    {
      "cargo_type": "Other",
      "rate": "0.015"
    }
  ]
}
# Test load rates from json request
response = requests.post(url, json=rates)
print(response.json())
# Test load rates from file
response = requests.get(url)
print(response.json())

# For insurance cost calculation
url = "http://localhost:8000/calculate_insurance"
date = "2020-06-01"
cargo_type = "Glass"
declared_value = 1000
# Test calculate insurance cost
response = requests.get(url, params={"date": date, "cargo_type": cargo_type, "declared_value": declared_value})
print(response.json())
