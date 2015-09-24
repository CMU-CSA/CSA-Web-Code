from django.core.management.base import NoArgsCommand
from django.contrib.auth.models import User
from VotingPlatform.models import AndrewIDs
from django.core.exceptions import ObjectDoesNotExist

class Command(NoArgsCommand):

    def add_arguments(self, parser):
        parser.add_argument('judge_id', nargs='+', type = str)

    def handle(self, *args, **options):
        for judge_id in options['judge_id']:
            try:
                AndrewIDs.objects.get(andrewId = judge_id)
            except ObjectDoesNotExist:
                judge = AndrewIDs(andrewId = judge_id, is_judge = True)
                judge.save()
