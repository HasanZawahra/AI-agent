import os
from functions.write_file import write_file

if __name__ == "__main__":
    os.makedirs("calculator", exist_ok=True)
    
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
