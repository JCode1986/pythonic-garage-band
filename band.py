# Use Python classes to model a Band made up of different kinds of musicians. Start with Guitarist,Bassist, and Drummer. Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.


class Band:
    all = []

    def __init__(self, name, members = []):
        self.name = name
        self.members = members
        self.__class__.all.append(self)

    #asks each member musician to play a solo, in the order they were added to band.
    def play_solos()
        pass

    def __repr__(self):
        return f'{self.name} - {self.members}'

    def __str__(self):
        return f'The Band\'s name is {self.name}, the members are {self.members}'

    # should return a list of previously created Band instances
    @classmethod
    def to_list():
        pass

    # should take in a collection of formatted data and returns a created Band instance. The Band instance should have its members be set to musicians based on info from the input.
    @staticmethod
    def create_from_data():
        pass

#Musician Subclass Tests
# Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
# Each kind of Musician instance should have a get_instrument method that returns string.
# Each kind of Musician instance should have a play_solo method that returns string.

class Musician:
    musician_list = []


class Guitarist(Musician):
    pass

class Bassist(Musician):
    pass

class Drummer(Musician):
    pass

