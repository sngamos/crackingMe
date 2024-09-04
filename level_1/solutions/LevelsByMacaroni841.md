# Amos' solution for LevelsByMacaroni841  

## Answer  
See LevelsByMacaroni841.py for functions to generate 1st and 2nd key pairs.  

## Preliminary checks  
1. First we can run the command `file LevelsByMacaroni841` and observe that the binary file is **not stripped**, hence we can use ghidra to decompile the file and examine its code.  

## Examining the code with ghidra  

1. we can go to the `main` function and observe that the code for the login logic is there, move on to analyze this code.  

2. We can quickly scan through the code and do some renaming of variables too.  
> `local-48` --> `input_string`  
> `sVar1` --> `string_length`  
> `local_10` --> `1st_string_length`  
> `local_78` --> `2nd-string`  
> `local_14` --> `2nd_string_length`
> `local_c` --> `index`  
> 

3. We also see that we need the string be something like `34xxxx`, a 5 character long string starting with `34`.  
> **Note**: although the decompiled code says 6 but we must take into account the presence of a NULL Terminator character.
4. Our 2nd string needs to have the same length as the first string, i.e 6 char long.  
5.  There is a for loop that iterates over all characters in the 2nd string and -48 from its ASCII encoding number. Then compares it to the first string's corresponding index character, -48 from this character, then mutiply by 2 the output of the subtraction.  
6. continue with bonus solve tmr