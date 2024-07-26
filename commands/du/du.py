import os

def convert_byte(byte):
    KB = byte / 1024
    MB = byte / (1024 * 1024)
    return KB, MB

def du(filename):
    if filename is None or not os.path.exists(filename):
        print("File not found.")
        return

    size = os.path.getsize(filename)
    byte = size    
    KB, MB = convert_byte(byte)
    print(str(byte) + " bytes")
    print(f"{round(KB, 2)} KB")
    print(f"{round(MB, 2)} MB")
    