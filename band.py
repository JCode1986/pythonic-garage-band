# Use Python classes to model a Band made up of different kinds of musicians. Start with Guitarist,Bassist, and Drummer. Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.

class Band:
    all_bands = []

    def __init__(self, name, musicians):
        self.name = name
        self.members = musicians
        self.__class__.all_bands.append(self)

    def __repr__(self):
        return f'The Band\'s name is {self.name}, and the members are {self.members}'

    def play_solos(self):
        pass

class Musician:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __repr__(self):
        return f'Musician: {self.name}'

#asks each member musician to play a solo, in the order they were added to band.
    @classmethod
    def play_solos(cls):
        pass

# should return a list of previously created Band instances
    @classmethod
    def to_list(cls):
        pass

    @staticmethod
    def create_from_data(data):
        pass

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def __repr__(self):
        return f'Guitarist: {self.name}'

    def __str__(self):
        return f'I am {self.name}, and I shred on the {self.get_instrument()}'

    def get_instrument(self):
        return 'Guitar'

    def play_solo(self):
        return '*shreds guitar with pick*'

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def __repr__(self):
        return f'Bassist: {self.name}'

    def __str__(self):
        return f'I am {self.name}, and I shred on the {self.get_instrument()}'

    def get_instrument(self):
        return 'Bass'

    def play_solo(self):
        return '*slaps bass*'

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def __repr__(self):
        return f'Drummer: {self.name}'

    def __str__(self):
        return f'I am {self.name}, and I shred on the {self.get_instrument()}'

    def get_instrument(self):
        return 'Drummer'

    def play_solo(self):
        return '*badum ch*'

if __name__ == '__main__':
    joe = Guitarist('Joe')
    print(joe)
    print(joe.play_solo())

    duke = Bassist('Duke')
    print(duke)
    print(duke.play_solo())

    leah = Drummer('Leah')
    print(leah)
    print(leah.play_solo())

    bob = Drummer('Bob')

    band_one = Band('Python shredders', [joe, duke, leah])
    band_two = Band('Generic Band', bob)
    print(band_one)
