from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from ..forms import LoginForm


class LoginClassView(LoginView):
    LoginView.authentication_form = LoginForm
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Sign in'

        return context
