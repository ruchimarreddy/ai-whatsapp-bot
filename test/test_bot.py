from app.bot import generate_reply


def test_generate_reply_returns_text() -> None:
    response = generate_reply("hello")
    assert isinstance(response.text, str)
    assert len(response.text) > 0
