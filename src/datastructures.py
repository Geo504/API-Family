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
        member["last_name"]= self.last_name
        member["id"] = self._generateId()
        self._members.append(member)


    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return self._members.remove(member)
        else:
            return None
        
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        else:
            return None

    def get_all_members(self):
        return self._members
