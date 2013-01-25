from helpers.sql_helpers import jsonize

__author__ = 'mjholler'

import webapp2
import json

import models.lots_model as lots_model


class Lots(webapp2.RequestHandler):

    def get(self):
        lots_table = lots_model.Lots()
        lots = lots_table.read_lots()

        if lots:
            self.response.write(jsonize(lots))
        else:
            self.response.set_status(204)
            self.response.write('204 No Content -- No Lots Exist')
