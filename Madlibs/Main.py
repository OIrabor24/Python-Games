import random 

# Story elements: names:(maybe) Nouns, verbs, adjectives and adverbs. 

# Nouns (A noun is an item, a thing.): fish, sock, tree, book, frisbee, rug, pillow,
#  tire,flower, ice, truck, plate, egg, blanket

# Verbs (A verb is an action word, something you do.): run, skip, hop, jump, walk, eat, drink, send, slurp, gallop, sweep, wrestle

# Adjectives (a word that describes a noun): flakey, old, blue, gree, red, transparent, beautiful, fluffy, new, sturdy, soft, crispy, purple

# Adverbs (describes a verb): quickly, carefully, swiftly, carelessly, slowly, curiously, 


def mad_libs1():
    """1st Mad Libs Generator."""

    name = input('Enter a name: ') 
    name_2 = input('Enter a 2nd name: ')
    name_3 = input('Enter a 3rd name: ')

    noun = input('Enter a noun: ')
    noun_2 = input('Enter a 2nd noun: ')
    noun_3 = input('Enter a 3rd noun: ') 

    verb = input('Enter a verb: ')
    verb_2 = input('Enter a 2nd verb: ')
    verb_3 = input('Enter a verb: ')

    adjective = input('Enter a adjective: ')
    adjective_2 = input('Enter a 2nd adjective: ')
    adjective_3 = input('Enter a 3rd adjective: ')

    adverb = input('Enter a adverb: ')
    adverb_2 = input('Enter a 2nd adverb: ')
    adverb_3 = input('Enter a 3rd adverb: ')

    print(
    f"Hey {name}, the family had just gotten to the {noun}, when they heard {verb} of distress coming from a {noun_2} near them."
    f"{name_2} jumped to his or her feet and {adverb} went to see what was the matter. {name_3} and the twins weren't far behind."

    f"{adverb_2} a crowd was forming around the distressed {noun_2}. {name} eyes following the {adjective} finger of the shrieking {noun_2}."
    f"On her {noun_3} he saw the {adjective_2} pile of {adjective_3} shit. {name} fainted. {name} had never seen anything like this before."
    f"Everyone was scared and afraid of the {adjective_3} pile of shit.{noun_2} was embarrassed to tell everyone about what happened."
    f"All eyes were on {noun_2}, as {noun_2} reached over and {adverb_2} pushed the {adjective_3} pile of shit on a woman's feet. Everyone cheered for {noun_2}. "
    f"{noun_2} {adverb_3 }became a local hero and legend. The woman cleaned her feet, and treated the whole family to dinner.")

mad_libs1() 

# Nouns (A noun is an item, a thing.); # Verbs (A verb is an action word, something you do.):; # Adjectives (a word that describes a noun):; # Adverbs (describes a verb):
def mad_libs2():
    """2nd Mad Libs Generator"""
    boys_name = input('Enter a name for a boy: ')
    a_type_of_packaging = input('Enter a name for a type of packaging: ')
    a_fashion_accessory = input('Enter the name of a fashion accessory (like a watch): ')
    a_place = input('Enter the name for a place: ')
    a_girls_name = input('Enter a name for a girl: ')
    park = input('Enter the name of a park: ')
    park_attraction = input('Enter the name of a park atrraction: ')
    number = input('Enter a number: ')
    names = input('Enter the names you chose for both boy and girl: ')
    

    print(f"Once upon a time there lived a very sad banana named {boys_name}. {boys_name} lived in a {a_type_of_packaging} in Fruitsville. " 
    f"He was sad because he had no friends, but then he thought, How am I going to get friends if I don't go looking for some? "
    f"I am going to go out and look for some friends. So {boys_name} put on his {a_fashion_accessory} to impress people and went out to {a_place}. He was walking around {a_place} when he met a nice lady banana called {a_girls_name}. "
    f"She said, Hello, my name is {a_girls_name}. Do you want to go to {park}, and go on the {park_attraction}? {boys_name} said, OK, If you will be my friend. Yes! She replied. "
    f"So {boys_name} and {a_girls_name} became good friends and {boys_name} wasn't sad anymore. "
    f"Later on they got married and had {number} little bananas called {names}. And they all lived happily ever after.")

mad_libs2() 



