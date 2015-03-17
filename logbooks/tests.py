from django.test import TestCase
import datetime
from django.utils import timezone


from logbook.models import Logbook, Log

class LogbookMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):	
        """
        was_published_recently() should return False for questions whose
        start_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Logbook(start_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_lobook = Logbook(pub_date=time)
        self.assertEqual(old_Logbook.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        old_logbook = Logbook(pub_date=time)
        self.assertEqual(old_logbook.was_published_recently(), True)