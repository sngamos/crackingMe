# Amos' solution for a.out

## Answer

## Preliminary investigation  

1. By running `file a.out`, we notice the binary is **not stripped**, this means we can go ahead to use ghidra to analyse the code.

## Examining code with ghidra  

1. Navigating to `main` function, we observe it calls `login` function
2. Investigating `login` function, we can observe that it creates 2 buffers, one of 8 bytes and another of 16 bytes.  
> Seems like we have to do a buffer overflow attack here.

continue from here to using debugger