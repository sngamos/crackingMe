# Amos' solution to crackMe1.bin file  

## Answer  
540
## Preliminary analysis  
We can use `file crackMe1.bin` command to check the binary of the file, and observe that the binary of this file is **not stripped**.  
We go ahead to use ghidra to decompile the file and examine the code.  

## Examining code with ghidra

1. We go to the `main` function and notice that it calls 2 other functions, `systemv` and `systemo` before returning 0. We also notice that `systemv` function's **decompiler** window outputs an empty function, so we can move past this for now and analyse `systemo`.  
2. We dig into `systemo` and screen through its decompiled code and do some renaming.  
> `local_18` --> `pw_input`  
> `local_14` --> `pw_string`   

3. We notice that we need to know what is the value of `local_c` and `local_10` in order to compute value of `pw_string`. We can go back to `systemv` function and observe the **Listing** window.
>         001009d4 c7 45 fc        MOV        dword ptr [RBP + local_c],0x5
>                 05 00 00 00
>        001009db c7 45 f8        MOV        dword ptr [RBP + local_10],0x7
>                07 00 00 00
>        001009e2 c7 45 f4        MOV        dword ptr [RBP + local_14],0x1f5
>                 f5 01 00 00  
4. From above we can see that value of `0x5` >> `local_c` and `0x7` >> `local_10`. Now that we know the values of `local_c` and `local_10` we can compute the value of `pw_string`.  
5. `pw_string` = (`local_c` * `local_10`) * `0x2d` = 540

