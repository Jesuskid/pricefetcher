#get the unit from a string
def get_substring(string):
    for sub in ['kg', 'gm', 'kilograms', 'grams', 'litres', 'ml', 'PACK', 'liter', 'Gms', 'pcs', 'gms']:
        stro = string.find(sub)
        if stro != -1:
            return sub
    return ''


#getb the quantity from a complex string
def get_quantity(string):
    res = [int(i) for i in string.split() if i.isdigit()]
    quantity = int(res[0])
    return quantity


#find price in float format
def get_float(string):
    print(string)
    res = [int(i) for i in string.split() if i.isdigit()]
    print(res)
    price = res[0]
    return price


#Split string to find the currency data
def get_currency(string):
    for sub in ['RS', 'GBP', 'USD', 'AUD', 'EU', 'ZA', '₹']:
        stro = string.find(sub)
        stro2 = string.find(sub.lower())
        stro3 = string.find(sub.capitalize())
        if stro != -1 or stro2 != -1 or stro3 != -1:
            if sub == '₹':
                sub = 'RS'
            return sub
    return ''


def get_city_for_dunzo(string):
    for i in ['Mumbai', 'Bangalore', 'Delhi', 'Chennai', 'Hyderabad', 'Pune']:
        sub_string = string.find(i)
        if sub_string != -1:
            return i

    return ''
