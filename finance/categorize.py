stations = ['shell', 'arco', 'chevron', 'fred m fuel']
grocerys = ['haggen', 'safeway', 'costco', 'fred meyer', 'snohomish apothecar']
boys = ['klahaya animal', 'everett pet']
supplements = ['ghost nv', 'super supplements']

# functions
def categorize(desc:str, amount:float):
    desclow = desc.lower()

    for station in stations:
        if station in desclow:
            if amount * -1 >= 10:
                return 'Gas'
            if amount * -1 < 9:
                return 'Snack'
    for grocery in grocerys:
        if grocery in desclow:
            return 'Grocery'
    for boy in boys:
        if boy in desclow:
            return 'Boys'
    return "Choose a category"