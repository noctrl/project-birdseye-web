__author__ = 'mjholler'
import webapp2
#from sqlalchemy import *
import sqlalchemy


class Lots(webapp2.RequestHandler):
    def get(self):
        sql = """
            SELECT * from birdseye.Lots;
        """
        engine = sqlalchemy.create_engine('mysql+pymysql://birdseye:password@localhost/birdseye')
        #engine = sqlalchemy.create_engine('mysql://birdseye:password@localhost/birdseye')
        conn = engine.connect()
        result = conn.execute(sql)
        conn.close()

        output = ""
        for row in result:
            output += str(row) + "<br />"
        self.response.write(str(output))

    def post(self):
        sql = """
            INSERT INTO birdseye.Lots (name, total_spaces) VALUES ('abcdefg', 60);
        """
        #engine = sqlalchemy.create_engine('mysql+pymysql://birdseye:password@localhost/birdseye')
        engine = sqlalchemy.create_engine('mysql+pymysql://birdseye:password@localhost/birdseye')
        conn = engine.connect()

        transaction = conn.begin()
        try:
            conn.execute(sql)
            transaction.commit()
            self.response.write('Worked!')

        except:
            transaction.rollback()
            self.response.write('You fucked shit up.!')





