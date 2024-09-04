# Amos' solution for a.out

## Answer
`00000000000000000000000000000000`
## Preliminary investigation  

1. By running `file a.out`, we notice the binary is **not stripped**, this means we can go ahead to use ghidra to analyse the code.

## Examining code with ghidra  

1. Navigating to `main` function, we observe it calls `login` function
2. Investigating `login` function, we can observe that it creates 2 buffers, one of 16 bytes and another of 8 bytes as seen from the **malloc** function.  
> however we do not know the distance between these buffers as malloc allocates memory in unknown locations.
3. Brute forcing works here as we know we need to change first bit in `puVar1` to 0, in order for the check to go to the `logged in as admin` portion.  
> refer to python script a_soln.py 
4. We observe that when 32 bytes of 0 are entered, we are able to login as admin, hence we know that the 2 buffers are 32 bytes apart.