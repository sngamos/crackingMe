import subprocess
import os
from pathlib import Path

path_to_revv = Path(__file__).parent.parent.parent / "problems"/ "revv"
for num in range(30):
    input_data = "A" * num
    run_binary = subprocess.run(path_to_revv,input=input_data,text=True,capture_output=True)
    print(f"{num}: {run_binary.stdout}")