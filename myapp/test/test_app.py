from app import *
import pytest

testdata = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output

testdata=[([7,6,5,4],[4,5,6,7]),([6,7,2,3],[2,3,6,7])]

@pytest.mark.parametrize('input, expected_output', testdata)
def test_bubblesort(input, expected_output):

    assert bubblesort(input) == expected_output
