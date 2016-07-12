"""
Prints out all the melons in our inventory
"""

from melons import melon_names, melon_seedlessness, melon_prices
"""
def print_melon(name, seedless, price):
    
    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print "{}s {} seeds and are ${:.2f}".format(name, have_or_have_not, price)
    """
def print_melon2():

    melons = {}
    for i in melon_names:
        melons[melon_names[i]] = {"seedless": melon_seedlessness[i], 
                                            "price": melon_prices[i]}

    #for melon, seed, cost in melons.interitems()

    #melon_dictionary['Casaba'] # {'p': 2, 's': T}

    for melon in melons:
        melons[melon]["flesh_color"] = None
        melons[melon]["weight"] = None
        melons[melon]["rind_color"] = None
# casaba = {'p': 2, 's': False}
# {'Casaba': {''}, 'Honey': {}}
    print melons

print_melon2()

