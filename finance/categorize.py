from category import *


# functions
def categorize(desc:str, amount:float):
    desclow = desc.lower()
    if amount > 0:
        return 'Income'
    for station in stations:
        if station in desclow:
            if amount < -10:
                return 'Auto, Gas'
            return 'Snack'
    for grocery in grocerys:
        if grocery in desclow:
            return 'Food, Grocery'
    for boy in boys:
        if boy in desclow:
            return 'Boys'
    for supplement in supplements:
        if supplement in desclow:
            return 'Supplements'
    for restaurant in restaurants:
        if restaurant in desclow:
            return 'Food, Dining'
    for selfcare in selfcares:
        if selfcare in desclow:
            return 'self-care'
    for utilitie in utilities:
        if utilitie in desclow:
            return 'utilites'
    for entertainent in entertainents:
        if entertainent in desclow:
            return 'entertainment'
    for saving in savings:
        if saving in desclow:
            return getSavings(saving,amount)
    return "Choose a category"