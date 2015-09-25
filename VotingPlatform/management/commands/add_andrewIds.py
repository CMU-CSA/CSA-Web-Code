from django.core.management.base import NoArgsCommand
from django.contrib.auth.models import User
from VotingPlatform.models import AndrewIDs
from django.core.exceptions import ObjectDoesNotExist

class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        txt_file = open("VotingPlatform/andrewids.txt","r")
        andrew_ids = txt_file.read().split(",")
        for andrew_id in andrew_ids:
            try:
                AndrewIDs.objects.get(andrewId = andrew_id)
                self.stdout.write('-- andrew ID: ' + andrew_id + 'already exists')
            except ObjectDoesNotExist:
                aid = AndrewIDs(andrewId = andrew_id)
                self.stdout.write('-- Audience andrew ID: ' + andrew_id + 'added')
                aid.save()
        self.stdout.write('-- andrew IDs scan complete')
