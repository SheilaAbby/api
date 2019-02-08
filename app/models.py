
from flask import Flask, request

from run import app

party_list = []


class PartyList:
    """This class represents the party model data"""
    def __init__(self, name, hdquarters, logourl):
        self.name = name
        self.hdquarters = hdquarters
        self.logoUrl = logourl

    def creating_party(self):

        data = request.get_json()

        party_item = {
            'id': len(party_list) + 1,
            'name': self.name,
            'hdQuaters': self.hdquaters,
            'logoUrl': self.logourl
        }
        self.register.append(party_item)




