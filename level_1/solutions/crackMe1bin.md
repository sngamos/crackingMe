# Amos' solution to crackMe1.bin file  

## Answer  

## Preliminary analysis  
We can use `file crackMe1.bin` command to check the binary of the file, and observe that the binary of this file is **not stripped**.  
We go ahead to use ghidra to decompile the file and examine the code.  

## Examining code with ghidra

1. We go to the `main` function and notice that it calls 2 other functions, `systemv` and `systemo` before returning 0. We also notice that `systemv` function does nothing, so we can ignore that function for now and investigate `systemo`.  
2. 