__author__ = 'mjholler'

import webapp2
from helpers.sql_helpers import jsonize
import models.lots_model as lots_model


class Lot(webapp2.RequestHandler):

    def get(self, lot_id):
        lots_table = lots_model.Lots()
        lot = lots_table.read_lot(lot_id)

        if lot:
            self.response.write(jsonize(lot))
        else:
            self.response.set_status(404)
            self.response.write("404 Not Found - lot_id = {id}".format(id=lot_id))
