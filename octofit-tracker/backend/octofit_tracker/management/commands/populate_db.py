from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **kwargs):
        # Clear existing data in correct order and only if objects exist
        for model in [Leaderboard, Activity, Workout, User, Team]:
            qs = model.objects.all()
            if qs.exists():
                for obj in qs:
                    obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], activity_type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='Yoga', duration=40, date=timezone.now().date())

        # Create workouts
        workout1 = Workout.objects.create(name='Full Body Workout', description='A complete workout for all muscle groups')
        workout2 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio session')
        workout1.suggested_for.set(users)
        workout2.suggested_for.set([users[0], users[2]])

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], score=120, rank=1)
        Leaderboard.objects.create(user=users[1], score=110, rank=2)
        Leaderboard.objects.create(user=users[2], score=105, rank=3)
        Leaderboard.objects.create(user=users[3], score=100, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
