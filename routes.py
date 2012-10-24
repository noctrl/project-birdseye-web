import webapp2

# Local imports
from handlers.test import test_handler
from handlers.rest import rest_handler

__author__ = 'mjholler'

app = webapp2.WSGIApplication([
    ('/', test_handler.HelloBirdseye),
    ('/api/rest/lots', rest_handler.lots),
    ('/api/rest/lot/[0-9]+', rest_handler.lot),
    ('/api/rest/sensors', rest_handler.sensors),
    ('/api/rest/sensor/[0-9]+', rest_handler.sensor)
], debug=True)
