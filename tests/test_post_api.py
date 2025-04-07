from api.placeholder_service import get_random_user, create_post_for_user

def test_create_post_using_user():
    user = get_random_user()
    user_id = user["id"]

    post = create_post_for_user(user_id)

    assert post["userId"] == user_id
    assert post["title"] == "Test Post"
