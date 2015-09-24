from django.core.management.base import NoArgsCommand
from django.contrib.auth.models import User
from VotingPlatform.models import AndrewIDs
from django.core.exceptions import ObjectDoesNotExist

class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        txt_file = open("VotingPlatform/andrewids.txt","r")
        lines = txt_file.read().split(",")
        for andrewid in lines:
            try:
                AndrewIDs.objects.get(andrewId = andrewid)
            except ObjectDoesNotExist:
                aid = AndrewIDs(andrewId = andrewid)
                aid.save()
