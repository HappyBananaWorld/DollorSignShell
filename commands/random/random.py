import random

def random_int(data):
    min_len = None
    max_len = None
    length = None

    if len(data) == 3:
        min_len = int(data[1])
        max_len = int(data[2])
    else:
        length = int(data[1])

    
    if length == None:
        return random.randint(min_len,max_len)

    # generate random int with len
    result = ""
    for i in range(length):
        result += str(random.randint(0,9))
    
    return result
    

def random_str(args):
    length = int(args[1])   
    capital_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letter = "abcdefghijklmnopqrstuvwxyz"
    symbol = "&*)(^%$#@!~/-+)"
    numbers = "1234567890"
    chars = capital_letter + small_letter + symbol + numbers

    result = ""
    for i in range(length):
        result += random.choice(chars)
    
    return result

def random_handle(args):
    try:
        type = args[0]    

        if type == "int":
            return print(random_int(args))
        if type == "float":
            return print(float(random_int(args)))
        if type == "string":
            return print(random_str(args))
    except ValueError:
        print("you are calling wrong command. pls type '$ random help' to show helper")
