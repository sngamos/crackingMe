import subprocess

from pathlib import Path
path_to_a = Path(__file__).parent.parent.parent / "problems"/ "a.out"

for num in range(33):
    input_data = b"\x00"*num
    print(input_data)
    run_binary = subprocess.run(path_to_a,input=input_data,capture_output=True)
    print(f"{num}: {run_binary.stdout}")