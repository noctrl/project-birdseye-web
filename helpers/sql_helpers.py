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

# TODO: Escape this stuff!!! Vunerable to SQL injections!
def generate_insert_sql(table, **kwargs):
    keys = '('
    values = '('

    for entry in kwargs:
        keys += '`%s`,' % entry
        values += "'%s'," % kwargs[entry]

    # remove trailing comma
    sql = 'INSERT INTO %(table)s %(keys)s VALUES %(values)s' % {'table': table,
                                                                'keys': keys[:-1] + ')',
                                                                'values': values[:-1] + ')'}
    return sql

if __name__ == '__main__':
    generate_insert_sql('lots', **{'name': 'steve', 'total_spaces': 67})


