# python script to generate 2nd strings for a given 1st string for this crackMe
import subprocess
from pathlib import Path
path_to_file = Path(__file__).parent.parent.parent / "problems"/ "LevelsByMacaroni841"


first_string = input("Input 5 character first string, starting with 34xxxx: ")
if len(first_string) != 5:
    print("Invalid length not 5")
    exit()
if first_string[:2] != "34":
    print("Invalid first 2 characters not 34")
    exit()
second_string = ""
for char in first_string:
    second_string += chr(((ord(char)-48)*2)+48)
print(f"Second string: {second_string}")
