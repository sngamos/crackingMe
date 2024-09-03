# Amos' solution for adventure

## Answer
`./adventure hello`  
`So, why are you here ? : ./adventure`

## Code breakdown

> Disclaimer code written in c

1. Replacing main function: 
replace `undefined8 main(int param_1,undefined8 *param_2)` --> `int main  
2. Understanding the main code:  

`param_2[1]` is an argument parsed into the program.  
> observe that `param_2[1]` is checked to be `"hello"` using strncmp function.  
> with this we know that `hello` needs to be parsed together when running the program to pass the first checkpoint.  

3. `__isoc99_scanf` function scans for user input in STDIN and stores it at variable `local_98`.  

4. Observe that `*param_2` is compared to `local_98` using `strncmp` function. 
> `*param_2` notice there isn't any index notion on this, usually this means it is the program name. i.e `./adventure`. 

5. From this we can tell to pass the 2nd checkpoint, we need to enter the program name, i.e `./adventure`.
