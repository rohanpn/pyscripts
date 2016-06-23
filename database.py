"""
    Database module
"""
import pymysql


class Database:
    """
        Database class
    """
    def __init__(self, host=None, user=None, pswd=None, db=None):
        self.host_name = host
        self.user_name = user
        self.password = pswd
        self.db_name = db
        self.db = ''
        self.cursor = ''
        self.error_msg = []

    def connect(self):
        """

        :return:
        """
        self.error_msg = []
        try:
            self.db = pymysql.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.password,
            )
            self.db.autocommit(1)
            self.cursor = self.db.cursor()

        except Exception:
            self.error_msg.append(
                "Unable to connect to database '" + self.db_name +
                "' of host '" + self.host_name + "' with user '" +
                self.user_name + "' and password '" + self.password + "'")
            return -1
        return 1

    def select_from_db(self, query):
        """

        :param query:
        :return:
        """
        self.error_msg = []
        iret = 0
        result = -1

        if not self.db:
            iret = self.connect()
        if iret == -1:
            return result

        try:
            result = self.cursor.fetchall()
        except Exception:
            self.error_msg.append("Failed executing select query '" + query + "'")
            result = -1

        return result

    def insert_update_to_db(self, query):
        """

        :param query:
        :return:
        """
        self.error_msg = []
        iret = 0
        result = -1
        if not self.db:
            iret = self.connect()
        if iret == -1:
            return result
        try:
            result = self.cursor.execute(query)
            self.db.commit()
            result = self.cursor.rowcount
        except Exception:
            self.db.rollback()
            self.error_msg.append("Failed executing insert query '" + query + "'")
            result = -1

        return result

    def disconnect(self):
        """

        :return:
        """
        print "disconnecting from database......"
        if self.db:
            self.db.close()

    def get_last_insert_id(self):
        """
        """
        return self.db.insert_id()

    def is_error(self):
        """

        :return:
        """
        if len(self.error_msg) > 0:
            return 1
        return 0

    def get_error(self):
        """

        :return:
        """
        return self.error_msg

