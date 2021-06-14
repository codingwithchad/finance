import re
def toFloat(amount):
    if '(' in amount:
        amount = amount.strip('()$')
        return float(amount) * -1
    else:
        amount = amount.strip('$')
        return float(amount)
