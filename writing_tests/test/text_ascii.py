from ..ascii import from_ascii_codes, to_ascii_codes
from hypothesis import given
from hypothesis.strategies import text

@given(text())
def test_decode_inverts(test_str:str) -> None:
    assert from_ascii_codes(to_ascii_codes(test_str)) == test_str
