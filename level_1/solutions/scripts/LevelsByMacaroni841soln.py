# python script to generate 2nd strings for a given 1st string for this crackMe
import subprocess
from pathlib import Path
path_to_file = Path(__file__).parent.parent.parent / "problems"/ "LevelsByMacaroni841"

def normal_solve():
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

def bonus_solve():
    input_string = "34"
    n = 6969 -1 -len(input_string)
    input_string += "0"* n
    print()