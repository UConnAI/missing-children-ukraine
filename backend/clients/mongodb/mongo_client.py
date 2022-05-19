import urllib.parse
from datetime import datetime
from typing import List

import pymongo

from models.models import ScheduleData, SurveyData


#Mongo client
class MongoClient():
    def __init__(self, user: str, password: str, database: str):
        """
        Initiate the pymongo to use with the MongoClient

        :param user: the mongo user to authenticate
        :param password: the mongo password to authenticate
        :param database: the database to write to
        """

        #encode the password into url
        pass_urlencoded = urllib.parse.quote(password)

        #Setup the pymongo mongo client
        self.client = pymongo.MongoClient(
            f"mongodb+srv://{user}:{pass_urlencoded}@missingchildrenukraine.nzlsq.mongodb.net/{database}?retryWrites=true&w=majority"
        )

        self.db = self.client[database]
