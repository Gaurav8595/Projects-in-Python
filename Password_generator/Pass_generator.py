#Random password Generator:
import random
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
while 1:
    pass_count = int(input("Enter the no. of password you want : "))
    pass_digit = int(input("Enter the no. of digit you want in yor password: "))
    for i in range(0, pass_count):
        password = ""
        for a in range(0, pass_digit):
            password_char = random.choice(alpha)
            password = password + password_char
        print("Yor password is : ", password)
    break