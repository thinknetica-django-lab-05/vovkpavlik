import json

from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from channels.generic.websocket import WebsocketConsumer

from main.models import Ad


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        try:
            ad = Ad.objects.get(name=message)
            self.send(text_data=json.dumps({
                'ad_id': ad.id,
                'ad_name': ad.name,
                'ad_url': reverse('ad-detail', kwargs={'slug': int(ad.id)})
            }))
        except ObjectDoesNotExist:
            self.send(text_data=json.dumps({
                'not_found': "Объявление не найдено",
            }))
