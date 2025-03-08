import json

from django.core.management.base import BaseCommand

from bot.models.tag import Tag

import os
from config.settings.common import DATA_DIR
import requests
from bot.bot_config import URL_BASE

class Command(BaseCommand):
    help = 'Load tags in tags.json file and update database'

    # def add_arguments(self, parser):
    #     parser.add_argument('jsonfile', type=str, help='Indicates the JSON file to export entities')

    def handle(self, *args, **options):
        response = requests.get(f'{URL_BASE}/api/v1/tag/')
        if response.status_code == 200:
            tag_list = json.loads(response.text)['tag']
            for tag_item in tag_list:
                tag, created = Tag.objects.get_or_create(id=tag_item['id'])
                tag.name = tag_item['name']
                tag.color = tag_item['color']
                print(f'Saving tag: {tag.name}, id: {tag.id} (New tag: {created})')
                tag.save()

            # Delete obsolete local tags
            saved_tags = Tag.objects.all()
            for tag_local in saved_tags:
                remote_tag = next((x for x in tag_list if x['id'] == tag_local.id), None)
                if not remote_tag:
                    print(f'Deleting tag: {tag_local}')
                    tag_local.delete()

