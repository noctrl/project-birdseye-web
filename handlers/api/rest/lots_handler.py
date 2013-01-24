__author__ = 'mjholler'

import webapp2
import json

import models.lots_model as lots_model
import helpers.sql_helpers as sql_helpers


class Lots(webapp2.RequestHandler):

    def get(self):
        lots_table = lots_model.Lots()
        lots = lots_table.read_lots()
        self.response.write(json.dumps(lots, default=sql_helpers.dthandler))

#        self.response.write(lots.json())
