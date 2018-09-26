import requests
import json
from jsonschema import validate


BASE_URL = "https://reqres.in"


def test_api():
    response = requests.get(BASE_URL + "/api/users")
    resp = json.dumps(response.json())
    json_schema = json.loads(resp)
    print(type(json_schema))
    assert response.status_code == 200


def test_api2():
    response = requests.get(BASE_URL + "/api/users", pa)
    resp = json.dumps(response.json())
    json_schema = json.loads(resp)
    assert json_schema['data'][0]['id'] == 1


def test_api3():
    with open('/Users/nikitachepurko/py_tuts/autotests/modules/schemas/resp.json', 'r') as f:
        schema1 = f.read()
    response = requests.get(BASE_URL + "/api/users")
    x = json.dumps(response.json())
    json_resp = json.loads(x)
    json_schema = json.loads(schema1)
    assert validate(json_resp, json_schema) is None


