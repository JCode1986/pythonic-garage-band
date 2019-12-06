# Use Python classes to model a Band made up of different kinds of musicians. Start with Guitarist,Bassist, and Drummer. Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.

class Band:
    band_members = []

    def __init__(self, name, members = []):
        self.name = name
        self.members = members
        self.__class__.band_members.append(self)

    def __repr__(self):
        return f'The Band\'s name is {self.name}, the members are {self.band_members}'

    @staticmethod
    def assemble_band():
        return "Python Shredders assemble!"

#asks each member musician to play a solo, in the order they were added to band.
    @classmethod
    def play_solos(cls):
        pass

# should return a list of previously created Band instances
    @classmethod
    def to_list(cls):
        pass

# should take in a collection of formatted data and returns a created Band instance. The Band instance should have its members be set to musicians based on info from the input.
    @staticmethod
    def create_from_data(data):
        pass
        # lines = data.split('\n')
        # leader_line = lines[0]
        # line_parts = leader_line.split(',')
        # musician_name = line_parts[0]
        # musician_instrument = line_parts[1]

        # if musician_name == 'Jimmy':
        #     musician_instrument = Guitarist(musician_name)

        # members = [Bassist('Davie504'), Drummer('Travis Barker')]
        # return Band(musician_instrument, members)

# Musician Subclass Tests
# Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
# Each kind of Musician instance should have a get_instrument method that returns string.
# Each kind of Musician instance should have a play_solo method that returns string.

class Musician(Band):
    musician_list = []
    def __init__(self, name, instruments):
        super().__init__(self)
        self.name = name
        self.instruments = instruments
        self.__class__.musician_list.append(self)

    @classmethod
    def get_members(cls):
        return cls.musician_list

    def __repr__(self):
        return f'Hi my name is {self.name}, and I shred on the {self.instruments}'

class Guitarist(Musician):
    def __init__(self, name, instrument):
        super().__init__(name)
        self.name = name
        self.instrument = instrument

    def play_solo(self):
        return '*shred guitar with pick*'

class Bassist(Musician):
    def __init__(self, name, instrument):
        super().__init__(name)
        self.name = name
        self.instrument = instrument

    def play_solo(self):
        return '*slaps bass*'

class Drummer(Musician):
    def __init__(self, name, instrument):
        super().__init__(name)
        self.name = name
        self.instrument = instrument

    def play_solo(self):
        return '*badum ch*'

if __name__ == '__main__':
    band_name = Band('Python Shredders', 'Chad')
    member_one = Guitarist('Jimmy', 'Guitar')
    member_two = Bassist('Davie504', 'Bass')
    member_three = Drummer('Travis Barker', 'Drummer')
    print(member_one)
    print(member_two)
    print(member_three)
    print(band_name)
