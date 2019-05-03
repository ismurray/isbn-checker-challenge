import pytest
from isbn_checker import IsbnChecker

def test_valid_isbn_10_checksum():
    assert IsbnChecker('0471958697').check() == True

def test_valid_isbn_10_with_trailing_x():
    assert IsbnChecker('097522980X').check() == True

def test_valid_isbn_10_with_spaces():
    assert IsbnChecker('0 471 60695 2').check() == True

def test_valid_isbn_10_with_dashes():
    assert IsbnChecker('0-471-60695-2').check() == True

def test_isbn_10_with_invalid_checksum():
    assert IsbnChecker('0471958699').check() == False

def test_isbn_10_with_invalid_length():
    assert IsbnChecker('04719586977').check() == False

def test_isbn_10_with_invalid_characters():
    assert IsbnChecker('04719X8697').check() == False

def test_valid_isbn_13_checksum():
    assert IsbnChecker('9780470059029').check() == True

def test_valid_isbn_13_with_spaces():
    assert IsbnChecker('978 0 471 48648 0').check() == True

def test_valid_isbn_13_with_dashes():
    assert IsbnChecker('978-0-13-149505-0').check() == True

def test_isbn_13_with_invalid_checksum():
    assert IsbnChecker('9780470059021').check() == False

def test_isbn_13_with_invalid_length():
    assert IsbnChecker('978047005902999').check() == False

def test_isbn_13_with_invalid_characters():
    assert IsbnChecker('978047005902X').check() == False
