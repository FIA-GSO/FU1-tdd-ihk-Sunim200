from ihk_rechner import ihk_noten_rechner
from ihk_rechner import ihk_noten_prozent
import pytest

def test_ihk_noten_rechner__type_error():
    # Arrange
    test_punkte  = "100"
    test_max_punkt = ""
    # Act
    with pytest.raises(TypeError):
        ihk_noten_rechner(test_punkte, test_max_punkt)


def test_ihk_noten_rechner__kleiner_als():
    test_punkte:int = -1
    test_max_punkte:int = -3
    with pytest.raises(ValueError):
        ihk_noten_rechner(test_punkte, test_max_punkte)

def test_ihk_noten_rechner__groesser_als():
    test_punkte = 101
    test_max_punkte = 100
    with pytest.raises(ValueError):
        ihk_noten_rechner(test_punkte, test_max_punkte)

def test_ihk_noten_rechner__bestanden():
    # Arrange
    test_punkte = 95
    test_max_punkte = 100
    test_erwartet = "sehr gut"
    ist = ihk_noten_rechner(test_punkte, test_max_punkte)
    assert test_erwartet == ist

def test_ihk_noten_rechner__nicht_bestanden():
    # Arrange
    test_punkte = 10
    test_max_punkte = 100
    test_erwartet = "ungenügend"
    # Act
    test_ist = ihk_noten_rechner(test_punkte, test_max_punkte)
    # Assert
    assert test_erwartet == test_ist

def test_ihk_noten_rechner__edge_bestanden():
    # Arrange
    test_punkte = 10
    test_max_punkte = 100
    test_erwartet = "ungenügend"
    # Act
    test_ist = ihk_noten_rechner(test_punkte, test_max_punkte)
    # Assert
    assert test_erwartet == test_ist

