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


def jsonize(obj):
    dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
    return json.dumps(obj, default=dthandler)

