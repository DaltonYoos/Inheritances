# This program demonstrates polymorphism.

import f_animals as animals

def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    gorilla = animals.Mammal('gorilla')
    #regular mamal instance
    dog = animals.Dog()
    #dog instance
    cat = animals.Cat()
    #cat instance

    '''
    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    gorilla.show_species()
    gorilla.make_sound()

    print()

    dog.show_species()
    dog.make_sound()

    print()

    cat.show_species()
    cat.make_sound()

    '''

    show_mamal_info(gorilla)
    show_mamal_info(dog)
    show_mamal_info(cat)
    show_mamal_info('bird')


def show_mamal_info(creature):
        if isinstance(creature,animals.Mammal):
            creature.show_species()
            creature.make_sound()
        
        else:
            print(creature, 'is not a mammal!')



# Call the main function.
main()
