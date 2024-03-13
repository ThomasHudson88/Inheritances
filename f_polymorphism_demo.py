# This program demonstrates polymorphism.

import f_animals as animals

def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()


    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    show_mammal_info(mammal)
    show_mammal_info(cat)
    show_mammal_info(dog)
    show_mammal_info('bird')

 

def show_mammal_info(animal):
        if isinstance(animal,animals.Mammal):
            animal.show_species()
            animal.make_sound()
            print()
        else:
             print(f"{animal} is not an Mammal!")
    

    #dog.show_species()
    #dog.make_sound()

    #cat.show_species()
    #cat.make_sound()

# Call the main function.
main()
