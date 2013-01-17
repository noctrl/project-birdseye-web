__author__ = 'mjholler'
import webapp2
#from sqlalchemy import *
import sqlalchemy


class Lots(webapp2.RequestHandler):
    def get(self):
        sql = """
            SELECT * from birdseye.Lots;
        """
        print 'hello'
        engine = sqlalchemy.create_engine('mysql+pymysql://birdseye:password@localhost/birdseye')
        #engine = sqlalchemy.create_engine('mysql://birdseye:password@localhost/birdseye')
        print '2'
        conn = engine.connect()
        print '3'
        result = conn.execute(sql)
        print '4'
        conn.close()
        print '5'

        output = ""
        for row in result:
            print "a row:",row
        self.response.write(result)

    def post(self):
        sql = """
            INSERT INTO birdseye.Lots (name, total_spaces) VALUES ('abcdefg', 60);
        """
        #engine = sqlalchemy.create_engine('mysql+pymysql://birdseye:password@localhost/birdseye')
        engine = sqlalchemy.create_engine('mysql://birdseye:password@localhost/birdseye')
        conn = engine.connect()

        transaction = conn.begin()
        try:
            conn.execute(sql)
            transaction.commit()
            self.response.write('Worked!')

        except:
            transaction.rollback()
            self.response.write('You fucked shit up.!')





