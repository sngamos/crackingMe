# Amos' solution for revv

## Answer  

## Preliminary checks  

1. First we can poke the file to check its behaviour using the `file revv` command.  
> observe that this binary is **stripped**, which means the debugging info is removed.

2. We can further poke the program with different inputs to test how their output behaviour differs.  
> see python script `revvsoln.py` for script.  
> this script tries different length of inputs from length 0 to 29.  
> Observe that from length 0 to 25, we get output of `Length mismatch! :(`, for length more than 25, we get `Don't try to hack me :D`. The only acception is when length == 21, where we get `Come on, Try Again! :(`.  