from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    MESSAGE = "AABBCC"
    INVALID_MSG = 5
    INVALID_KEY = "K"

    assert encrypt_message(MESSAGE, 3) == "BAA_CCB"
    assert encrypt_message(MESSAGE, 4) == "CC_BBAA"
    assert encrypt_message(MESSAGE, -1) == "CCBBAA"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(MESSAGE, INVALID_KEY)

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(INVALID_MSG, 3)
