#1. class Patient {id, name}
class Patient:
    def __init__(self, id, name):
        self.id = id 
        self.name = name 
    def __str__(self):
        return f'[id={self.id}, name={self.name}]'
    def __repr__(self):
        return self.__str__()