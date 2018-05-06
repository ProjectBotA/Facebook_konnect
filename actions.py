from rasa_core.actions import Action
from rasa_core.events import SlotSet
from sqlalchemy import create_engine
import pymysql

engine = create_engine('mysql+pymysql://root:root123@localhost/ProjDB', echo=True)
conn = engine.connect()

class ActionSearchNGOName(Action):
    def name(self):
        return 'action_search_ngo_name'
    def run(self, dispatcher, tracker, domain):
        name = tracker.get_slot('name')
        query = "select * from ngos where name = {0}".format(name)
        res = conn.execute(query).fetchall()
        print(name)

class ActionDonateOnline(Action):
    def name(self):
        return 'action_donate_online'
    def run(self, dispatcher, tracker, domain):
        print('You are being redirected for online donation')
    #Payment gateway integration here

    

