#Recreation of PleaseCrackMe in python

username = input("Type in your username: ")
number = int(input("Type in a number between 1 and 9: "))
if number<1:
    print("Error number is too small")
elif number < 10:
    zero = 0
    pw_arr =[None]*32
    while True:
        counter = zero
        print("counter", counter)
        username_length = len(username)
        if username_length <= counter:
            break
        pw_arr[counter] = chr(number+ord(username[zero]))
        zero +=1
    pw_string = ""
    for i in pw_arr:
        if i != None:
            pw_string+=i
    print(pw_string)
    pw_input = input("Type in the password: ")
    if (pw_string == pw_input):
        print("You are successfully logged in")
    else:
        print("Wrong password")
else:
    print("Number is too big")
