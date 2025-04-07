from api.poetry_service import get_poems_by_author, search_poems_by_word

def test_get_poems_by_author():
    poems = get_poems_by_author("Shakespeare")
    assert isinstance(poems, list)
    assert all("Shakespeare" in poem.get("author", "") for poem in poems)

def test_search_poems_by_word():
    poems = search_poems_by_word("hope")
    assert isinstance(poems, list)
    assert any(
        "hope" in line.lower()
        for poem in poems
        for line in poem.get("lines", [])
    )
