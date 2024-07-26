# $.py

import sys
from commands.cat.cat import cat

class DollorSign:
    def __init__(self) -> None:
        self.command = None
        self.values = None
        self.extract()

    # extract argument, command, value
    def extract(self):
        arguments = sys.argv[1:]
        command = arguments[0]
        value = arguments[1:]

        self.command = command
        self.values = value

    def main(self):
        self.check_command()
        
        # debug
        # print(self.command)
        # print(self.values)
        
    def check_command(self):
        if self.command == "cat":
            cat(self.values[0])

if __name__ == "__main__":
    dollorsign = DollorSign()
    dollorsign.main()
