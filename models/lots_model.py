
__author__ = 'mjholler'

import json
import datetime

from sqlalchemy import text

import database
from helpers.sql_helpers import generate_insert_sql


class Lots:

    def __init__(self):
        self.engine = database.engine
        self.meta = database.meta
        # odd need to be lowercase
        self.table = self.meta.tables['lots']

    def read_lots(self):
        sql = """SELECT * FROM lots"""
        result = self.engine.execute(text(sql))

        return [dict(row) for row in result]

    def read_lot(self, lot_id):
#        result = self.engine.execute(self.table.select(self.table.c.lot_id == lot_id))
        result = self.engine.execute('select * from lots where lot_id = %s', lot_id)

        lot = result.fetchone()
        return dict(lot) if lot else None

    def create_lot(self, **kwargs):
        sql = generate_insert_sql('lots', **kwargs)

        result = self.engine.execute(sql)

#        sql = """INSERT INTO lots (`name`, `description`, `location`, `spaces_available`, `total_spaces`)
#                 VALUES (%(name)s, %(description)s, %(location)s, %(spaces_available)s, %(total_spaces)s)
#        """

#        result = self.engine.execute(sql)


