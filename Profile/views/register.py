from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView
from ..forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super(RegisterView, self).form_valid(form)

        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')

        user = authenticate(self.request, email=email, password=password)

        if user:
            user.set_password(password)
            user.save()

        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
