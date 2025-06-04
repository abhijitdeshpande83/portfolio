from django.core.management.base import BaseCommand
from NLPGenHub.cron_job import cleanup_task

class Command(BaseCommand):
    help = 'Runs the cleanup task'

    def handle(self, *args, **options):
        cleanup_task(stdout=self.stdout, style=self.style)
