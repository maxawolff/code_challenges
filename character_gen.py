"""Character Generator for an RPG."""
import sys


class Character(object):
    """A character object for a rpg like skyrim."""

    def __init__(self, name, _class):
        """Initialization for the character object."""
        self.name = name
        self._class = _class
        self.stats = {}
        self.equipment = {}
        self.abilities = {}

    class Weapon(object):
        """."""

        def __init__(self, name, _range, damage, energy, bonuses):
            """Initialization for a weapon, mele, ranged, or magic."""
            self.name = name
            self.range = _range
            self.damage = damage
            self.energy = energy
            # As in how much energy it take to use the weapon

    class Armour(object):
        """."""

        def __init__(self, name, defense, weight, bonuses):
            """Initialization for a weapon, mele, ranged, or magic."""
            self.name = name
            self.defense = defense
            self.weight = weight

    class Warrior(object):
        """The fighter class used to generate stats."""

        def __init__(self):
            import random
            self.name = 'warrior'
            self.stats = {}
            self.stats['hp'] = random.randint(8, 13)
            self.stats['stamina'] = random.randint(6, 11)
            self.stats['strength'] = random.randint(8, 13)
            self.stats['speed'] = random.randint(4, 9)
            self.equipment = {}

        def equip(self, item):
            """Add an item to a character."""
            self.equipment[item.name] = item

    class Mage(object):
        """The fighter class used to generate stats."""

        def __init__(self):
            import random
            self.name = 'mage'
            self.stats = {}
            self.stats['hp'] = random.randint(7, 12)
            self.stats['mana'] = random.randint(9, 14)
            self.stats['power'] = random.randint(4, 9)
            self.stats['speed'] = random.randint(5, 10)
            self.equipment = {}

        def equip(self, item):
            """Add an item to a character."""
            self.equipment[item.name] = item

    class Rouge(object):
        """The fighter class used to generate stats."""

        def __init__(self):
            import random
            self.name = 'rouge'
            self.stats = {}
            self.stats['hp'] = random.randint(6, 11)
            self.stats['stamina'] = random.randint(5, 10)
            self.stats['strength'] = random.randint(6, 11)
            self.stats['speed'] = random.randint(8, 13)
            self.equipment = {}

        def equip(self, item):
            """Add an item to a character."""
            self.equipment[item.name] = item


def prompt_user(question, number):
    """Prompt the user to answer a given question."""
    reply = input(question)
    if reply.lower() == 'q' or reply == 'quit':
        sys.exit()
    elif validate_question(number, reply):
        return reply
    else:
        print("that reply was invalid, try again")
        return prompt_user(question, number)

creation_questions = [
    'What is the name of your character', 'What class would you like to play as? The choices are warrior, mage, or rouge?'
]

valid_classes = ['warrior', 'mage', 'rouge']


def validate_question(question, input):
    """Given a question, determine if input is valid."""
    if question == 0:
        if type(input) == str:
            return True
        else:
            return False
    else:
        if input.lower() in valid_classes:
            return True
        else:
            return False


def generate_character():
    """Prompt the user to create a character from the terminal."""
    name = prompt_user(creation_questions[0], 0)
    _class = prompt_user(creation_questions[1], 1)
    user_char = Character(name, _class)
    import pdb; pdb.set_trace()
    print('Welcome, ' + user_char.name, + 'the ' + user_char._class.name)
    print('Your stats are: ')
    for stat in user_char._class.stats:
        print(stat)
