# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import pytest

from morse_converter import encrypt
from morse_converter import decrypt


def test_encrypt_returns_correct_value():
    message = "Hello world"
    encrypted_message = "....   .   .-..   .-..   ---       .--   ---   .-.   .-..   -.."
    assert encrypt(message) == encrypted_message


def test_encrypt_raises_value_error_with_invalid_characters():
    invalid_message = "€#¢∞¡"
    with pytest.raises(KeyError):
        encrypt(invalid_message)


def test_encrypt_raises_value_error_if_invalid_type_given():
    invalid_type = 100
    with pytest.raises(ValueError):
        # noinspection PyTypeChecker
        encrypt(invalid_type)


def test_decrypt_returns_correct_decrypted_message():
    message = "hello world"
    encrypted_message = "....   .   .-..   .-..   ---       .--   ---   .-.   .-..   -.."
    assert decrypt(encrypted_message) == message


def test_decrypt_raises_value_error_when_invalid_type_given():
    invalid_message = 100
    with pytest.raises(ValueError):
        # noinspection PyTypeChecker
        decrypt(invalid_message)


def test_decrypt_raises_key_error_when_invalid_character_given():
    invalid_message = "Hello world"
    with pytest.raises(KeyError):
        decrypt(invalid_message)
