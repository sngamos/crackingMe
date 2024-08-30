
# Amos' solution for level1  

## Answer  
Password is **sudo0xl8**  

## Code breakdown  

> Disclaimer: code written in c  

1. Replacing main function:  
replace `undefined8 main(void)` --> `int main(void)`  
2. Understanding the main code:  

`iVar1 = checkPass(local_48)`  
> Invokes function `checkPass`, we need to investigage `checkPass`.

3. Investigating `checkPass`  
> `*param_1 == 's'` checks if param_1[0] is 's'  
> Then attach value of param[1] to cVar1.
> Then check `cVar1[1]=='u'`  
> repeat above for remainding elements of param_1.  
> We can tell that checkPass checks for string **sudo0xl8** and returns a success if this string is param_1.
