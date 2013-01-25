
__author__ = 'mjholler'

import json
import datetime

from sqlalchemy import text

import database


class Lots:

    def __init__(self):
        self.engine = database.engine
        self.meta = database.meta
        self.table = self.meta.tables['Lots']

    def read_lots(self):
        sql = """SELECT * FROM Lots"""
        result = self.engine.execute(text(sql))

        return [dict(row) for row in result]

    def read_lot(self, lot_id):
#        result = self.engine.execute(self.table.select(self.table.c.lot_id == lot_id))
        result = self.engine.execute('select * from lots where lot_id = %s', lot_id)

        lot = result.fetchone()
        return dict(lot) if lot else None

