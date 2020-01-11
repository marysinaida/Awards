from django.test import TestCase
from .models import Author, Project

# Create your tests here.


class AuthorTestClass(TestCase):
    # set up method
    def setUp(self):
        self.mary = Author(first_name='mary', last_name='Snyder',
                           email='marydorcassinaida54@gmail.com')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.mary, Author))
# Testing Save Method

    def test_save_method(self):
        self.mary.save_author()
        author = Author.objects.all()
        self.assertTrue(len(author) > 0)


def test_get_projects_today(self):
    today_projects = Project.todays_projects()
    self.assertTrue(len(today_projects) > 0)


def test_get_projects_by_date(self):
    test_date = '2017-03-17'
    date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
    projects_by_date = Project.days_projects(date)
    self.assertTrue(len(projects_by_date) == 0)
