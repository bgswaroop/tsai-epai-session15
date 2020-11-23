import inspect
import os
import re

import session15
from session15 import *


def test_readme_exists():
    """
    Check if the README file exists
    :return: None
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test the length of the README file
    :return: None
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 200, "Make your README.md file interesting! Add at least 200 words"


def test_readme_file_for_formatting():
    """
    Tests the formatting for the README file
    :return: None
    """
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    """
    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
    :return: None
    """
    functions = inspect.getmembers(session15, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_fetch_data():
    """
    Try exhausting the generator
    :return: None
    """

    parking_tickets = fetch_data()
    for _ in parking_tickets:
        pass

    try:
        next(parking_tickets)
    except StopIteration as e:
        pass
    else:
        assert False

    assert True


def test_compute_violations_by_car():
    """
    Test the number of violations by car brand
    :return: None
    """

    output = compute_violations_by_car_make()

    if output:
        assert True
    else:
        assert False