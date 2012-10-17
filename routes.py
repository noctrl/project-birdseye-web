import webapp2

# Local imports
from handlers.test import test_handler

__author__ = 'mjholler'

app = webapp2.WSGIApplication([
    ('/', test_handler.HelloBirdseye),
], debug=True)
