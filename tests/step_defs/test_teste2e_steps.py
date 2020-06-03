import json
import logging

import pytest
import requests
from jsonpath_ng import parse
from pytest_bdd import given, when, parsers, scenarios, then

scenarios('../features/teste2e.feature')

# Logger information
logger = logging.getLogger(__name__)

api_endpoints = {}
request_headers = {}
response_codes = {}
response_texts = {}
request_bodies = {}
request_id = {}
api_url: str = "https://reqres.in/"


@pytest.fixture(scope="module")
def read_json_file():
    f = open("tests/data.json", )
    data = json.load(f)
    logger.info(data)
    f.close()
    return data


@given(parsers.parse('i enter the url as {phrase}'))
def step_impl(phrase):
    global api_url
    api_url = phrase
    logger.info(api_url)


@given(parsers.parse('set the resource as POST with request body and parameters {phrase}'))
def step_impl(phrase, read_json_file):
    api_endpoints['POST_URL'] = api_url + phrase;
    request_bodies['POST'] = read_json_file
    pass


@when(parsers.parse('request is {phrase}'))
def step_post_implementation(phrase):
    response = requests.post(url=api_endpoints['POST_URL'], json=request_bodies['POST'])
    response_texts['POST'] = response.text
    print("post response :" + response.text)
    # extracting response status_code
    response_codes['POST'] = str(response.status_code)
    logger.info("Implemented " + response_texts['POST'])


@then(parsers.cfparse("i validate the response and check status code as {status:Number}", extra_types=dict(Number=int)))
def step_validate_response(status):
    json_string = ''.join(response_texts['POST'])
    json_data = json.loads(json_string)
    name = parse('$.name')
    id = parse('$.id')
    name_match = name.find(json_data)
    id_match = id.find(json_data)
    string_value = str(name_match[0].value)
    request_id['id'] = ''.join(id_match[0].value)
    logger.info("ID value is " + id_match[0].value)
    assert status == 201
    assert string_value.__contains__("morpheus")


@given("there was a successful POST")
def step_successful_post():
    response = requests.get(url=api_url + "api/users/" + request_id['id'],
                            headers=request_headers)
    response_codes['GET'] = response.status_code


@then("i assert the get response")
def step_get():
    assert response_codes['GET'] == 404
