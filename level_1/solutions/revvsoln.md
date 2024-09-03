# Amos' solution for revv

## Answer  
`ACTF{N01ce_R3v3r51^g}`
## Preliminary checks  

1. First we can poke the file to check its behaviour using the `file revv` command.  
> observe that this binary is **stripped**, which means the debugging info is removed.

2. We can further poke the program with different inputs to test how their output behaviour differs.  
> See python script `revvsoln.py` for script.  
> This script tries different length of inputs from length 0 to 29.  
> Observe that from length 0 to 25, we get output of `Length mismatch! :(`, for length more than 25, we get `Don't try to hack me :D`. The only acception is when length == 21, where we get `Come on, Try Again! :(`.  

## Examining the code with ghidra  

1. Since the binary is **stripped**, we will not be able to find the **main** function, hence we search `entry` to identify where the program starts.  
2. After clicking around on some of the functions that the `entry` function calls, we find that `FUN_001013ba` seems to be of interest. We will rename this to `this_is_main`.  
3. From the `this_is_main` function we can observe it asks for user input `Enter the Password: ` like what we observed in part 2 of our preliminary check
4. Now we see that `this_is_main` function calls another function `FUN_001011c9`, which is fed with the user input. This is likely the verification function, so we rename it to `verify_func`.  
5. Inspect the `verify_func` and walah, we dug out the verification logic. Now we just need to decode the answer from the mix of hex and integers.  
> We can see that the sequence of characters for params is: `A,C,T,F,{,N,0,1,c,e,_,R,3,v,3,r,5,1,^,g,}`