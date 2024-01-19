
from django.urls import path
from django.views.decorators.csrf import csrf_exempt



from bot.views.main import AemBotView
urlpatterns = [
    path('webhook-telegram/', csrf_exempt(AemBotView.as_view())),
]
