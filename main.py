from flask import Flask, flash, redirect, render_template, request, session, abort, Response, jsonify
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
import requests
import json
import pymysql 
from rasa_core.agent import Agent

app = Flask(__name__)
app.secret_key = 'avavdacacac'
dialogue_location = 'C:/Users/Inspiron/Desktop/Project8/rasa/rasa_files/models/dialogue'
model_location = 'C:/Users/Inspiron/Desktop/Project8/rasa/rasa_files/models/default/model_20180501-231024'
db_connection_string = 'mysql+pymysql://root:root123@localhost/ProjDB'
engine = create_engine(db_connection_string, echo=True)
agent = Agent.load(dialogue_location, interpreter = model_location)
conn = engine.connect()
    
@app.route('/login', methods=['POST'])
def do_admin_login():
 
    POST_USERNAME = str(request.json['username'])
    POST_PASSWORD = str(request.json['password'])
 
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = 1
        return Response("Authorization successfull", status = 200)
    else:
        return Response("Authorization not successfull", status = 403)

@app.route('/register/', methods=['POST'])
def register():
    Session = sessionmaker(bind=engine)
    s = Session()
    user = User(request.json['username'] , request.json['email'], request.json['password'])
    s.add(user)
    s.commit()
    return Response('User successfully registered', status=200)

     
@app.route("/logout", methods=['GET'])
def logout():
    session['logged_in'] = 0
    return Response("Logged out successfully", status=200)

@app.route("/details", methods=['POST'])
def get_details():
    data = request.json
    for_ret = []
    query_type = data['type']
    field_name = data['field_name']
    if query_type == 'full_details':
        #for getting full details of the NGO by ngo name
        query = "select * from ngo_details where NGO_name = '{0}'".format(field_name)
        print(query)
    if query_type == 'ngo_aim':
        #for getting ngos working for a particular area (education etc. stored in NGO_aim)
        query = "select * from ngo_aim where NGO_aim = '{0}'".format(field_name)

    res = conn.execute(query).fetchall()
    for row in res:
        for item in row:
            for_ret.append(str(item))
    payload = {'results':for_ret}
    return jsonify(payload)

def extract_info(s):
    extracted_entities = []
    extracted_intent = ''
    payload = {'q':s}
    r = requests.post('localhost:5000/parse', json=json.dumps(payload))
    data = r.json()
    
    for item in data["entities"]:
        temp = {}
        temp["name"] = item["entity"]
        temp["value"] = item["value"]
        extracted_entities.append(temp)

    extracted_intent = data["intent"]["value"] if data["intent"]["confidence"] > 0.50 else None
    return extracted_intent, extracted_entities
    
    
@app.route("/get_info")
def info():
    answer = ''
    auth = request.authorization
    username = auth.username
    if session['logged_in'] == 1:
        query = request.args['query']
        answer = agent.handle_message(query, sender_id = username)
    return jsonify(answer)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)