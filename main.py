# Library Management System V1
# Author: Koos
# Date: 15/11/2025


import sqlite3
from manager.library_manager import LibraryManager

def main():
    manager = LibraryManager()
    manager.main_menu()

if __name__ == "__main__":
    main()