import requests

params = {
    "amount" : 10,
    "type" : "boolean"
}

api_call = "https://opentdb.com/api.php?amount=10&type=boolean"
response = requests.get(api_call)
response.raise_for_status()
json_res = response.json()

question_data = json_res["results"]