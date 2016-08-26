from django.core.management.base import BaseCommand, CommandError
import requests
import json
from polls.models import UserStatus

class Command(BaseCommand):
    def handle(self, *args, **options):
        r = requests.get('https://private-86ccf-users169.apiary-mock.com/list')

        dtaReturned = r.json()
        for userJo in dtaReturned["members"]: 
            q = UserStatus(user_id=userJo["id"], status=userJo["presence"])
            q.save()
