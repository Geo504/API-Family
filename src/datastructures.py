from random import randint
import uuid

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

    def _generateId(self):
        id = uuid.uuid4()
        return str(id)

    def add_member(self, member):
        self._members.append({"first_name": member["first_name"], "last_name": self.last_name, "id": self._generateId()})

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return self._members.remove(member)
            return member
        
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member

    def get_all_members(self):
        return self._members
