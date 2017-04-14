"""An adoption system maintenance tool for an animal shelter.

This shelter contains cats and dogs. Hopeful adopters can only adopt
pets by following these strict guidelines:

* If you don't specify a species, you adopt the animal who's been in the
  shelter for the longest amount of time.

* If you specify cat, you get the cat who's lived there the longest.

* If you specify dog, you get the dog who's lived there the longest.

Examples:

    >>> shelter = AnimalShelter()

    >>> fluffy = Cat("Fluffy")
    >>> ginger = Cat("Ginger")
    >>> duchess = Cat("Duchess")
    >>> fido = Dog("Fido")
    >>> rover = Dog("Rover")

    >>> shelter.take_in(fluffy)
    >>> shelter.take_in(fido)
    >>> shelter.take_in(duchess)
    >>> shelter.take_in(ginger)
    >>> shelter.take_in(rover)

    >>> shelter.introduce_next_pet().name
    'Fluffy'

    >>> adopted_pet = shelter.release_animal_to_owner()
    >>> adopted_pet.name
    'Fluffy'

    >>> shelter.introduce_next_pet().name
    'Fido'

    >>> adopted_cat = shelter.release_animal_to_owner("cat")
    >>> adopted_cat.name
    'Duchess'

    >>> adopted_dog = shelter.release_animal_to_owner("dog")
    >>> adopted_dog.name
    'Fido'

"""

from pets import Cat, Dog
from queue_ll import Queue
import datetime

class AnimalShelter():
    """A place for animals to be cared for until they're adopted."""

    def __init__(self):

        self.cats = Queue()
        self.dogs = Queue()

    def take_in(self, animal):
        """Take a pet in until it's adopted."""

        # Is there a better way to handle the timing?

        if type(animal) == Cat:
            self.cats.enqueue((animal, datetime.datetime.now()))

        elif type(animal) == Dog:
            self.dogs.enqueue((animal, datetime.datetime.now()))
            self.dogs.peek()

        else:
            print("We don't take that kind of animal here, sorry!")


    def introduce_next_pet(self):
        """Show an interested owner the next pet up for adoption."""

        next_cat = self.cats.peek()
        next_dog = self.dogs.peek()

        if next_cat[1] < next_dog[1]:
            return next_cat[0]

        else:
            return next_dog[0]

    def release_animal_to_owner(self, species=None):
        """Let a person adopt a pet."""

        if species is not None: 
            if species.lower() == "cat":
                return self.cats.dequeue()[0]

            elif species.lower() == "dog":
                return self.dogs.dequeue()[0]

        else:
            next_cat = self.cats.peek()
            next_dog = self.dogs.peek()

            if next_cat[1] < next_dog[1]:
                return self.cats.dequeue()[0]

            else:
                return self.dogs.dequeue()[0]


            




