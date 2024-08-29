# Amos' solution for easyAF  

## Answer  
Password is **"pass"**  

## Code breakdown  

> Disclaimer: code written in c++  

1. Replacing main function:  
replace `ulong main(void)` --> `int main(void)`  
2. Understanding the code:  

`basic_string<> local_68 [32]`  
> array of 32 `std: :basic_string<>` objects.  
Likely a placeholder from decompilation, possibly representing a single string.  

`basic_string local_48 [40]`
> array of 40 `std::basic_string<>` objects.  
Likely a single string.  

`long local_20`  
> long represent whole 32 bit integers, int usually 16 bit
`local_20` used for storing value to check for stack corruption.  

`local_20 = *(long *)(in_FS_OFFSET + 0x28)`  
> initialize `local_20` to value of `in_FS_OFFSET` + `0x28`.  

`std::__cxx11::basic_string<>::basic_string()`  
> constructor call for `std::basic_string` class from c++ standard library.  

`std::__cxx11::basic_string<>::operator=(local_68,"pass")`
> assign **"pass"** to `local_68`, can be seen from `operator=` function.  

`std::operator<<((basic_ostream *)std::cout,"Enter the password: ")`  
> prints "Enter the password" to console , i.e STDOUT (`std::cout`)  

`std::operator>>((basic_istream *)std::cin,local_48)`  
> read inputs from console, i.e STDIN (`std::cin`) the store it in `local_48`  

`uVar3 = std::operator==()`  
> compares `local_48` with `local_68`, can tell from `operator==` function, then assign this result to variable uVar3.  

`if ((char)uVar3 == '\0')`  
> casts value of uVar3 to a `char` object, then compare to `\0` (null or false).  
> Basically, this if statement runs if `local_48` == `local_68` results in false.  

`uVar2 = std::operator!=()`  
> comparison operator using `!=` operator, checks if seems redunant. Output of this operation assigned to `uVar2`.

`if ((char)uVar2 != '\0')`  
> `uVar2` cast to `char` type object, then compared to `\0` using != logic. 

`std::operator<<((basic_ostream *)std::cout,"Nope")`  
> print to console **Nope** if password is not correct  

`std::operator<<((basic_ostream *)std::cout,"Welldone!")`  
> print to console **Welldone!** when password match and the else block above this line is ran.

From this we conclude that the password is **pass**.









