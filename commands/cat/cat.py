def cat(filename):
    result = None
    with open(filename,'r') as file:
        result = file.read()
        print(result)
        return result