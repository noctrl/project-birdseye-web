import webapp2
from helpers import test_helper


from config import config_parse

__author__ = 'mjholler'

class HelloBirdseye(webapp2.RequestHandler):
    def get(self):
        self.response.write(test_helper.stupid_function())
