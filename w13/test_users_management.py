from users_management import user_create_validation
import pytest


def test_user_create_validation():
    assert not user_create_validation({'name': ''})
    assert user_create_validation({'name': 'Vitor', 'username': 'vitormb', 'password': '123'})


pytest.main(["-v", "--tb=line", "-rN", __file__])
