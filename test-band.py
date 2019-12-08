from band import Band, Musician, Guitarist, Bassist, Drummer
# , Musician, Guitarist, Bassist, Drummer
import pytest

band_one = Band('Python Band', [Bassist('Curly Noproblem')])
band_two = Band('Typescript Band', [Drummer('Stricto Mcgee')])
band_three = Band('Javasciptt Band', [Guitarist('Loosey Whatever')])

def test_band_instance_string_attr():
    """
    A Band instance should have a name attribute which is a string
    """
    expected = 'Python Band'
    actual = band_one.name
    assert expected == actual

def test_members_attribute_from_band():
    """
    A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
    """
    # expected = [Drummer: Stricto Mcgee]
    # actual = band_two.members
    # assert expected == actual
    pass


def test_play_solos_method():
    """
    A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
    """
    pass

def test_band_str_and_repr():
    """
    A Band instance should have appropriate __str__ and __repr__ methods.
    """
    # expected = f'The Band\'s name is {band_two.name}, and the members are {band_two.members}'
    # actual = band_two
    # assert expected == actual
    pass

def test_to_list_method():
    """
    A Band should have a class method to_list which returns a list of previously created Band instances
    """
    # expected = [The Band's name is Python Band, and the members are [Bassist: Curly Noproblem], The Band's name is Type Script Band, and the members are [Drummer: Stricto Mcgee]]
    # actual = Band.get_bands()
    # assert expected == actual
    pass

def test_static_method_from_data():
    """
    A Band should have a static method create_from_data which takes a collection of formatted data and returns a created Band instance. The Band instance should have its members be set to musicians based on info from the input.
    """
    pass

def test_musician_str_and_repr():
    """
    Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
    """
    # expected = 'Guitarist: foo'
    # actual = Guitarist('foo')
    # print(type(actual))
    # assert actual == expected
    pass

def test_get_instrument():
    """
    Each kind of Musician instance should have a get_instrument method that returns string.
    """
    jon = Guitarist('Jon Snow')
    cersei = Bassist('Cersei')
    little_finger = Drummer('Little Finger')
    band_lst = [jon.get_instrument(), cersei.get_instrument(), little_finger.get_instrument()]
    actual = jon.get_instrument()
    expected = 'Guitar'
    assert actual == expected

# def test_musician_solo():
#     """
#     Each kind of Musician instance should have a play_solo method that returns string.
#     """
#     
#     


