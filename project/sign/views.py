from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'sign/index.html'


from django.views import View
from django.contrib.auth.forms import AuthenticationForm

class LoginFormView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'sign/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            # Добавьте свою логику для обработки введенных данных формы
            return render(request, 'success.html')
        return render(request, 'sign/login.html', {'form': form})
