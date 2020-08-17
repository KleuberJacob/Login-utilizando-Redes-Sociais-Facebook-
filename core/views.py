from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin  # Quando quisermos que para acesar determinada view seja
# obrigatório realizar login nesse caso acesando o index, onde caso nao esteja logado será redirecionado para página
# de login


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'



