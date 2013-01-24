__author__ = 'mjholler'

import webapp2
import json

import models.lots_model as lots_model
import helpers.sql_helpers as sql_helpers


class Lot(webapp2.RequestHandler):

    def get(self, lot_id):
        lots_table = lots_model.Lots()
        lot = lots_table.read_lot(lot_id)

        if lot:
            self.response.write(json.dumps(lot, default=sql_helpers.dthandler))
        else:
            self.response.set_status(404)
            self.response.write("404 Not Found - lot_id = {id}".format(id=lot_id))
