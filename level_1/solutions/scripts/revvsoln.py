import subprocess
import os
from pathlib import Path
path_to_revv = Path(__file__).parent.parent.parent / "problems"/ "revv"
for num in range(33):
    input_data = "A" * num
    #print(input_data)
    run_binary = subprocess.run(path_to_revv,text =True,input=input_data,capture_output=True)
    print(f"{num}: {run_binary.stdout}")