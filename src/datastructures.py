
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):  # Esto define qué va a ser la clase. Le va a asignar lo que tenga esta función, o sea un last name y members.
        self.last_name = last_name  # Self es una palabra reservada de Python.

        # example list of members
        self._members = [{"id": self._generate_id(),
                        "first_name": "John",
                        "last_name": last_name,
                        "age" : 32,
                        "lucky_numbers" : [7, 13, 22]
                        },
                        {"id": self._generate_id(),
                        "first_name": "Jane",
                        "last_name": last_name,
                        "age" : 35,
                        "lucky_numbers" : [10, 14, 3]
                        },
                        {"id": self._generate_id(),
                        "first_name": "Jimmy",
                        "last_name": last_name,
                        "age" : 5,
                        "lucky_numbers" : [1]
                        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member['id'] = self._generate_id()
        member['last_name'] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        for item in self._members:
            if item['id'] == id:
                position = self._members.index(item)
                del self._members[position]
                return self._members
        return False

    def get_member(self, id):
        for item in self._members:
            if item['id'] == id:
                return item
        return False

    def modify_member(self, member, id):
        member['id'] = id
        member['last_name'] = self.last_name
        for item in self._members:
            if item['id'] == id:
                position = self._members.index(item)
                self._members[position] = member
        return False
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
