import pytest
from isbn_checker import IsbnChecker

def test_valid_isbn_ten_checksum():
    assert IsbnChecker('0471958697').check() == True

def test_valid_isbn_ten_with_trailing_x():
    assert IsbnChecker('097522980X').check() == True

def test_valid_isbn_ten_with_spaces():
    assert IsbnChecker('0 471 60695 2').check() == True

def test_valid_isbn_ten_with_dashes():
    assert IsbnChecker('0-471-60695-2').check() == True

def test_isbn_ten_with_invalid_checksum():
    assert IsbnChecker('0471958699').check() == False

def test_isbn_ten_with_invalid_length():
    assert IsbnChecker('04719586977').check() == False

def test_isbn_ten_with_invalid_characters():
    assert IsbnChecker('04719X8697').check() == False
