from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Workouts
        avengers_workout = Workout.objects.create(name='Avengers HIIT', description='High intensity workout for Marvel team', difficulty='Hard')
        justice_workout = Workout.objects.create(name='Justice League Strength', description='Strength workout for DC team', difficulty='Medium')

        # Create Users (Superheroes)
        users = [
            User(email='tony@marvel.com', username='Tony Stark', team=marvel, is_superhero=True),
            User(email='steve@marvel.com', username='Steve Rogers', team=marvel, is_superhero=True),
            User(email='bruce@dc.com', username='Bruce Wayne', team=dc, is_superhero=True),
            User(email='clark@dc.com', username='Clark Kent', team=dc, is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create Activities
        from datetime import datetime
        activities = [
            Activity(user=users[0], workout=avengers_workout, date=datetime(2025, 12, 1, 8, 0), duration_minutes=30, calories_burned=300),
            Activity(user=users[1], workout=avengers_workout, date=datetime(2025, 12, 1, 9, 0), duration_minutes=45, calories_burned=400),
            Activity(user=users[2], workout=justice_workout, date=datetime(2025, 12, 1, 10, 0), duration_minutes=60, calories_burned=500),
            Activity(user=users[3], workout=justice_workout, date=datetime(2025, 12, 1, 11, 0), duration_minutes=50, calories_burned=200),
        ]
        for activity in activities:
            activity.save()

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=1900, rank=2)
        Leaderboard.objects.create(team=dc, total_points=2100, rank=1)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
