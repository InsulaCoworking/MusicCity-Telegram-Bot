
import json
from threading import Thread

from django.http import JsonResponse
from django.views import View
from telegram import Update


class AemBotView(View):

    def post(self, request, *args, **kwargs):

        from ..apps import dispatcher, bot

        body = json.loads(request.body)
        print("POST RECEIVED")
        print(body)
        thread = Thread(target=dispatcher.process_update, args = [Update.de_json(body, bot)])
        thread.start()
        return JsonResponse({"ok": "POST request processed"})

