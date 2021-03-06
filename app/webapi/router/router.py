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

@app.route("/room/condition", methods=["GET"])
def getroomcondition():

    if request.args.get("name") == None:
        return jsonify({"result": "failed"})

    r = RoomConditionConnector()

    if request.args.get("startdate") != None and request.args.get("enddate") != None:
        startdate = datetime.strptime(request.args["startdate"], "%Y-%m-%d %H:%M:%S")
        enddate = datetime.strptime(request.args["startdate"], "%Y-%m-%d %H:%M:%S")
        data = r.select_room_condition(name=request.args["name"], startdate=startdate, enddate=enddate)
        room_conditions = RoomConditions([RoomCondition(d[0], d[1], d[2], d[3].strftime("%Y-%m-%d %H:%M")) for d in data])
        result = room_conditions.get_all_dict()
        return jsonify(result)

    if request.args.get("startdate") != None:
        startdate = datetime.strptime(request.args["startdate"], "%Y-%m-%d %H:%M:%S")
        data = r.select_room_condition(name=request.args["name"], startdate=startdate)
        room_conditions = RoomConditions([RoomCondition(d[0], d[1], d[2], d[3].strftime("%Y-%m-%d %H:%M")) for d in data])
        result = room_conditions.get_all_dict()
        return jsonify(result)

    data = r.select_room_condition(name=request.args["name"])
    room_conditions = RoomConditions([RoomCondition(d[0], d[1], d[2], d[3].strftime("%Y-%m-%d %H:%M")) for d in data])
    result = room_conditions.get_all_dict()
    return jsonify(result)

@app.route("/human/condition", methods=["GET"])
def gethumancondition():

    if request.args.get("name") == None:
        return jsonify({"result": "failed"})

    h = HumanConditionConnector()

    if request.args.get("startdate") != None and request.args.get("enddate") != None:
        startdate = datetime.strptime(request.args["startdate"], "%Y-%m-%d %H:%M:%S")
        enddate = datetime.strptime(request.args["startdate"], "%Y-%m-%d %H:%M:%S")
        data = h.select_human_condition(name=request.args["name"], startdate=startdate, enddate=enddate)
        human_conditions = HumanConditions([HumanCondition(d[0], d[1], d[2], d[3], d[4], d[5].strftime("%Y-%m-%d %H:%M")) for d in data])
        result = human_conditions.get_all_dict()
        return jsonify(result)

    if request.args.get("startdate") != None:
        startdate = datetime.strptime(request.args["startdate"], "%Y-%m-%d %H:%M:%S")
        data = h.select_human_condition(name=request.args["name"], startdate=startdate)
        human_conditions = HumanConditions([HumanCondition(d[0], d[1], d[2], d[3], d[4], d[5].strftime("%Y-%m-%d %H:%M")) for d in data])
        result = human_conditions.get_all_dict()
        return jsonify(result)

    data = h.select_human_condition(name=request.args["name"])
    human_conditions = HumanConditions([HumanCondition(d[0], d[1], d[2], d[3], d[4], d[5].strftime("%Y-%m-%d %H:%M")) for d in data])
    result = human_conditions.get_all_dict()
    return jsonify(result)

@app.route("/user", methods=["POST"])
def registeruser():
    u = UserConnector()
    u.insert_user(name=request.form["name"])

    data = u.select_user(name=request.form["name"])
    return jsonify(data)

@app.route("/room/condition", methods=["POST"])
def postroomcondition():
    r = RoomConditionConnector()

    if "temperature" in request.form.keys() and "humidity" in request.form.keys():
        temperature = request.form["temperature"]
        humidity = request.form["humidity"]
        r.insert_room_condition(name=request.form["name"], temperature=temperature, humidity=humidity)

    return jsonify([{"result": "success"}])

@app.route("/human/condition", methods=["POST"])
def posthumancondition():
    h = HumanConditionConnector()
    if "heart" in request.form.keys() and "steps" in request.form.keys() and "distance" in request.form.keys() and request.form.keys():
        heart = request.form["heart"]
        steps = request.form["steps"]
        distance = request.form["distance"]
        calories = request.form["calories"]
        h.insert_human_condition(name=request.form["name"], heart=heart, steps=steps, distance=distance, calories=calories)

    return jsonify([{"result": "success"}])
