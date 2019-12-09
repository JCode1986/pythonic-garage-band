# Use Python classes to model a Band made up of different kinds of musicians. Start with Guitarist,Bassist, and Drummer. Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.

class Band:
    all_bands = []

    def __init__(self, name, musicians = None):
        self.name = name
        self.members = musicians
        self.__class__.all_bands.append(self)

    def __repr__(self):
        return f'The Band\'s name is {self.name}, and the members are {self.members}'
    
    @staticmethod
    def assemble_band():
        return 'let\'s get this party started!'

    @classmethod
    def get_bands(cls):
        return cls.all_bands

class Musician(Band):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __repr__(self):
        return f'Musician: {self.name}'

    def get_instrument(self):
        return self.__class__.instrument_of_choice

    def play_solo(self):
        return self.__class__.solo_performance

    @classmethod
    def to_list(cls):
        pass

    @staticmethod
    def create_from_data(data):
        pass

class Guitarist(Musician):
    instrument_of_choice = 'Guitar'
    solo_performance = '*shreds guitar with pick*'

    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def __repr__(self):
        return f'Guitarist: {self.name}'

    def __str__(self):
        return f'I am {self.name}, and I shred on the {self.__class__.instrument_of_choice}'

class Bassist(Musician):
    instrument_of_choice = 'Bass'
    solo_performance = '*slaps bass*'

    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def __repr__(self):
        return f'Bassist: {self.name}'

    def __str__(self):
        return f'I am {self.name}, and I shred on the {self.__class__.instrument_of_choice}'

class Drummer(Musician):
    instrument_of_choice = 'Drummer'
    solo_performance = '*badum ch*'

    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def __repr__(self):
        return f'Drummer: {self.name}'

    def __str__(self):
        return f'I am {self.name}, and I shred on the {self.__class__.instrument_of_choice}'

if __name__ == '__main__':
    joe = Guitarist('Joe')
    print(joe)

    duke = Bassist('Duke')
    print(duke)

    leah = Drummer('Leah')
    print(leah)

    bob = Drummer('Bob')

    band_one = Band('Python shredders', [joe, duke, leah])
    assert len(band_one.members) == 3, 'band_one should be 3 members'
    band_two = Band('Generic Band', bob)
    print(band_one)
    assert len(Band.all_bands) == 2, 'should be 2'
    print(Band.get_bands())
    print(Band.play_solos())
