import pytest

from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.urls import reverse

from .factories import UserFactory

from ..models import User
from ..views import DetailUser, EditUser, RedirectUser

pytestmark = pytest.mark.django_db


class TesEditUser:

    def test_get_success_url(self, user: User, rf: RequestFactory):
        view = EditUser()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_success_url() == f"/users/{user.username}/"

    def test_get_object(self, user: User, rf: RequestFactory):
        view = EditUser()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_object() == user


class TestRedirectUser:

    def test_get_redirect_url(self, user: User, rf: RequestFactory):
        view = RedirectUser()
        request = rf.get("/fake-url")
        request.user = user

        view.request = request

        assert view.get_redirect_url() == f"/users/{user.username}/"


class TestDetailUser:

    def test_authenticated(self, user: User, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = UserFactory()
        view = DetailUser.as_view()
        response = view(request, username=user.username)

        assert response.status_code == 200

    def test_not_authenticated(self, user: User, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = AnonymousUser()
        view = DetailUser.as_view()
        response = view(request, username=user.username)
        login_url = reverse(settings.LOGIN_URL)

        assert response.status_code == 302
        assert response.url == f"{login_url}?next=/fake-url/"
