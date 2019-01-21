# Sample Test passing with nose and pytest

import base64

from jinja2 import Environment

import pytest


@pytest.fixture
def environment():
    return Environment(extensions=["jinja2_base64_filters.Base64Filters"])


@pytest.fixture()
def my_string():
    return "teststring"


@pytest.fixture()
def my_b64_encoded_string(my_string):
    return base64.b64encode(my_string.encode()).decode()


def test_b64encode(environment, my_string, my_b64_encoded_string):
    template = environment.from_string("{{teststring|b64encode}}")

    rdr = template.render(teststring=my_string)

    assert rdr == my_b64_encoded_string


def test_b64decode(environment, my_string, my_b64_encoded_string):
    template = environment.from_string("{{testb64string|b64decode}}")

    rdr = template.render(testb64string=my_b64_encoded_string)

    assert rdr == my_string
