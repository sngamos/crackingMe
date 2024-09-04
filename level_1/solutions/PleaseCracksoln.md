# Amos' solution for PleaseCrackMe  

## Answer  
See PleaseCrackMesoln.py for a simple python script that replicates this program.  
## Preliminary checks  
1. First we can poke the file to check its behaviour using the `file PleaseCrackMe` command.  
> observe that this binary is **not stripped**, which means we can use ghidra to analyze the decompiled code.

## Analysing using ghidra  

1. Navigating to `main` function we see that the login logic can be found there.  

2. We can do some renaming while scanning through the code:  
> `local_78` --> `username`    
> `local_80` --> `number`    
> `local_7c` --> `zero`  
> `uVar4` --> `counter`  
> `sVar3` --> `username_length`  
> `local_58` --> `pw_string`  
> `local_38` --> `pw_input`  

3. We then see that 1 < `number`< 10.  

4. The main logic for generating the password comes from `pw_string[zero] = (char)number + username[zero]`, which is basically a shift cipher.  
> the shift cipher generates a password by shifting each character in the username by `number` key spaces in ASCII encoding.  
> **Note**: in C when a `char` is used in arithmetic operation, it is implicitly converted to its ASCII value.  


