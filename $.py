# $.py

import sys
from commands.cat.cat import cat
from commands.getip.ip import ipv4, ipv6, ip

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
            return cat(self.values[0])
        
        if self.command == "ipv4":
            return ipv4()
        
        if self.command == "ipv6":
            return ipv6()
        
        if self.command == "ip":
            return ip()
            
        

if __name__ == "__main__":
    dollorsign = DollorSign()
    dollorsign.main()
