from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from customauth.forms import (
    UserLoginForm,
)


class UserLogin(LoginView):
    authentication_form = UserLoginForm
    template_name = "login.html"
    redirect_authenticated_user = True
    next_page = "/"


class UserLogout(LogoutView):
    next_page = "/login/"


class PasswordChangeView(PasswordChangeView):
    pass


class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = ""
    next_page = "/"
