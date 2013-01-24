__author__ = 'mjholler'

import datetime
import json


def row2dict(row):
    d = {}
    for col in row.__table__.columns:
        d[col.name] = getattr(row, col.name)
    return d


def result2array(result):
    a = []
    for row in result:
        a.append(row2dict(row))
    return a


class DBRow(dict):
    def __init__(self, *args, **kw):
        super(DBRow, self).__init__(*args, **kw)

    def json(self):
        dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
        return json.dumps(self, default=dthandler)

if __name__ == '__main__':
    a = DBRow({'hello': 'steve'})
    print a.json()

