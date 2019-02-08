
from flask import Flask, request

from run import app

party_list = []


class PartyModel:
    """This class represents the party model data"""
    def __init__(self):
        self.db = party_list

    def creating_party(self, name, hqaddress, logourl):
        party_item = {
            "id": len(self.db) + 1,
            "name": self.name,
            "hqAddress": self.hqaddress,
            "logoUrl": self.logourl
        }
        self.db.append(party_item)
        return self.db


