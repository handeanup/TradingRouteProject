import pytest

from django.contrib.auth import get_user_model
User = get_user_model()

@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('8095819801', 'anup', 'hande')
  assert User.objects.count() == 1
