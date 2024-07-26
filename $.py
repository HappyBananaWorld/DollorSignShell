# $.py

import sys
import time
import pyperclip
from commands.cat.cat import cat
from commands.getip.ip import ipv4, ipv6, ip
from commands.random.random import random_int,random_handle

class DollorSign:
    def __init__(self) -> None:
        self.command = None
        self.values = None
        self.isCopy = False
        self.copyKey = "--copy"
        self.extract()

    # extract argument, command, value
    def extract(self):
        arguments = sys.argv[1:]

        if arguments[-1] == self.copyKey:
            self.isCopy = True
            arguments.pop()
            
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
        return_data = ""

        if self.command == "cat":
            return_data = cat(self.values[0])
        
        if self.command == "ipv4":
            return_data = ipv4()
        
        if self.command == "ipv6":
            return_data = ipv6()
        
        if self.command == "ip":
            return_data = ip()
        
        if self.command == "random":
            return_data = random_handle(self.values)

        if self.isCopy:
            pyperclip.copy(str(return_data))
            print('copied...')
        return return_data
        

if __name__ == "__main__":
    dollorsign = DollorSign()
    dollorsign.main()
