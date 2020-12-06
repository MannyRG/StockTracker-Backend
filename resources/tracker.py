import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

# We can use this as a Python decorator for routing purposes
# first argument is blueprints name
# second argument is it's import_name
track = Blueprint('tracked', 'track')



@track.route('/track', methods=["GET"])
def get_all_tracks():
    ## find the dogs and change each one to a dictionary into a new array
    try:
        #  Fetching data from personal API
        trackers = [model_to_dict(stock) for stock in models.Tracker.select()]
        print(trackers)
        return jsonify(data=trackers, status={"code": 200, "message": "Tracker was requested"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting Tracker"})


@track.route('/track', methods=["POST"])
def new_track():
    payload = request.get_json()
    print(type(payload), 'payload')
    # Creating models table on tracked stocks
    # stock = models.Tracker.create(**payload)
    new_track = models.Tracker.create()
    print(model_to_dict(new_track), 'model to dict')
    new_track_dict = model_to_dict(new_track)
    return jsonify(data=new_track_dict, status={"code": 201, "message": "Success New Ticker in Tracker"})

@track.route('/track/<id>', methods=["PUT"])
def update_track(id):
    payload = request.get_json()
    print(type(payload), 'payload')
    payload = request.get_json()
    # Update models table on tracked stocks
    # stock = models.Tracker.create(**payload)
    query = models.Tracker.update(**payload).where(models.Tracker.id==id)
    query.execute()
    updated_track = model_to_dict(models.Tracker.get_by_id(id))
    return jsonify(data=updated_track, status={"code": 201, "message": "Success New Ticker in Tracker"})



@track.route('/track/<id>', methods=["DELETE"])
def delete_track(id):
    delete_query = models.Tracker.delete().where(models.Tracker.id == id)
    deleted_tracks = delete_query.execute()
    print(deleted_tracks)
    return jsonify(
    data={},
    message="Successfully deleted {} post with id {}".format(deleted_track, id),
    status={"code": 200, "message": "Success"}
    )













