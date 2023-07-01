import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


jackson_family = FamilyStructure("Jackson")
jackson_family.add_member({"first_name": "John"})
jackson_family.add_member({"first_name": "Jane"})
jackson_family.add_member({"first_name": "Jimmy"})

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return jsonify(response_body)


@app.route('/members/<string:member_id>', methods=['GET'])
def handle_get_member(member_id):
    members = jackson_family.get_all_members()
    for member in members:
        if member["id"]==member_id:
            return jsonify(member)


@app.route('/members', methods=['POST'])
def handle_add_member():
    members = jackson_family.get_all_members()
    request_body = request.json
    jackson_family.add_member(request_body)
    return "done"


@app.route('/members/<string:member_id>', methods=['DELETE'])
def handle_delete_member(member_id):
    members = jackson_family.get_all_members()
    for member in members:
        if member["id"]==member_id:
            members.remove(member)
    return "done"


if __name__ == '__main__':
    # PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=3000, debug=True)
