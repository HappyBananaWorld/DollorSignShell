def cat(filename):
    with open(filename,'r') as file:
        print(file.read())