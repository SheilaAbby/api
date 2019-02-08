from flask import Blueprint, request, make_response, jsonify

from app import models

party = models.PartyModel

# make blueprint

app_route = Blueprint('politico-v1', __name__, url_prefix='/api/v1/')

# create a party
app_route.route('/parties', methods=['POST'])


class Party(party):
    def __init__(self):
        self.db = party


def post_party(self):
    party_data = request.get_json()
    name = party_data.get('name')
    logourl = party_data.get('logourl')

    res = self.db.creating_party(name, logourl)
    return make_response(jsonify({
        "status": 201,
        "data": res
    })), 201
