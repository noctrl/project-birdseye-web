import webapp2

# Local imports
from handlers.test import test_handler
from handlers.api.rest import lots_handler

__author__ = 'mjholler'

app = webapp2.WSGIApplication([
    ('/', lots_handler.Lots),
], debug=True)
