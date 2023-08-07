import pytest

from fortune_function import first_name_valid


def test_first_name():

    assert first_name_valid("johnathan") == True


def test_first_name_with_numbers():

    assert first_name_valid("12345") == False


def test_first_name_with_a_surname():

    assert first_name_valid("john appleseed") == False
