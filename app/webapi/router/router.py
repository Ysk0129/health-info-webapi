from webapi import app
from flask import request
from flask import jsonify
from datetime import datetime
from webapi.db.room_condition_connector import RoomConditionConnector
from webapi.db.human_condition_connector import HumanConditionConnector
from webapi.db.user_connector import UserConnector
from webapi.models.room_condition import RoomCondition
from webapi.models.room_conditions import RoomConditions
from webapi.models.human_condition import HumanCondition
from webapi.models.human_conditions import HumanConditions

@app.route("/getroomcondition", methods=["POST"])
def getroomcondition():
    r = RoomConditionConnector()

    if "startdate" in request.form.keys() and "enddate" in request.form.keys():
        startdate = datetime.strptime(request.form["startdate"], "%Y-%m-%d %H:%M:%S")
        enddate = datetime.strptime(request.form["startdate"], "%Y-%m-%d %H:%M:%S")
        data = r.select_room_condition(name=request.form["name"], startdate=startdate, enddate=enddate)
        room_conditions = RoomConditions([RoomCondition(d[0], d[1], d[2], d[3]) for d in data])
        result = room_conditions.get_all_dict()
        return jsonify(result)

    if "startdate" in request.form.keys():
        startdate = datetime.strptime(request.form["startdate"], "%Y-%m-%d %H:%M:%S")
        data = r.select_room_condition(name=request.form["name"], startdate=startdate)
        room_conditions = RoomConditions([RoomCondition(d[0], d[1], d[2], d[3]) for d in data])
        result = room_conditions.get_all_dict()
        return jsonify(result)

    data = r.select_room_condition(name=request.form["name"])
    room_conditions = RoomConditions([RoomCondition(d[0], d[1], d[2], d[3]) for d in data])
    result = room_conditions.get_all_dict()
    return jsonify(result)

@app.route("/gethumancondition", methods=["POST"])
def gethumancondition():
    h = HumanConditionConnector()

    if "startdate" in request.form.keys() and "enddate" in request.form.keys():
        startdate = datetime.strptime(request.form["startdate"], "%Y-%m-%d %H:%M:%S")
        enddate = datetime.strptime(request.form["startdate"], "%Y-%m-%d %H:%M:%S")
        data = h.select_human_condition(name=request.form["name"], startdate=startdate, enddate=enddate)
        human_conditions = HumanConditions([HumanCondition(d[0], d[1], d[2], d[3], d[4], d[5]) for d in data])
        result = human_conditions.get_all_dict()
        return jsonify(result)

    if "startdate" in request.form.keys():
        startdate = datetime.strptime(request.form["startdate"], "%Y-%m-%d %H:%M:%S")
        data = h.select_human_condition(name=request.form["name"], startdate=startdate)
        human_conditions = HumanConditions([HumanCondition(d[0], d[1], d[2], d[3], d[4], d[5]) for d in data])
        result = human_conditions.get_all_dict()
        return jsonify(result)

    data = h.select_human_condition(name=request.form["name"])
    human_conditions = HumanConditions([HumanCondition(d[0], d[1], d[2], d[3], d[4], d[5]) for d in data])
    result = human_conditions.get_all_dict()
    return jsonify(result)

@app.route("/registeruser", methods=["POST"])
def registeruser():
    u = UserConnector()
    u.insert_user(name=request.form["name"])

    data = u.select_user(name=request.form["name"])
    return jsonify(data)

@app.route("/postroomcondition", methods=["POST"])
def postroomcondition():
    r = RoomConditionConnector()

    if "temperature" in request.form.keys() and "humidity" in request.form.keys():
        temperature = request.form["temperature"]
        humidity = request.form["humidity"]
        r.insert_room_condition(name=request.form["name"], temperature=temperature, humidity=humidity)

    return jsonify([{"result": "success"}])

@app.route("/posthumancondition", methods=["POST"])
def posthumancondition():
    h = HumanConditionConnector()
    if "heart" in request.form.keys() and "steps" in request.form.keys() and "distance" in request.form.keys() and request.form.keys():
        heart = request.form["heart"]
        steps = request.form["steps"]
        distance = request.form["distance"]
        calories = request.form["calories"]
        h.insert_human_condition(name=request.form["name"], heart=heart, steps=steps, distance=distance, calories=calories)

    return jsonify([{"result": "success"}])
