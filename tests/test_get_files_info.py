import os
from functions.get_files_info import get_files_info

if __name__ == "__main__":
    os.makedirs("calculator", exist_ok=True)
    
    print(get_files_info("calculator", "."))
    print(get_files_info("calculator", "pkg"))
    print(get_files_info("calculator", "/bin"))
    print(get_files_info("calculator", "../"))
