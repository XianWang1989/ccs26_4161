
import os

if not os.path.exists(os.path.expanduser(DATABASE)):
    print("Database file does not exist.")
