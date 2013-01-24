import webapp2

# Local imports
from handlers.api.rest import lots_handler
from handlers.api.rest import lot_handler

__author__ = 'mjholler'

app = webapp2.WSGIApplication([
    ('/api/rest/lots', lots_handler.Lots),
    ('/api/rest/lot/(\d+)', lot_handler.Lot),
#    ('/api/rest/sensors', sensors_handler.Sensors),
#    ('/api/rest/sensor', sensors_handler.Sensors),
], debug=True)
