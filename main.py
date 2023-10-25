'''
Lab 6: Version Control
Benjamin Gold
'''

def encoder(num_string):
    int_string = ""
    for i in range(0, len(num_string)):
        new_num = int(num_string[i]) + 3
        if new_num > 9:
            new_num = str(int(num_string[i] - 10))
        int_string += str(new_num)
    return int_string

def decoder():
    print("hi")

if __name__ == '__main__':
    run = True
    encoded_pass = ""
    decoded_pass = ""
    while run:
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")
        user_input = input("Please enter an option: ")
        if user_input == "1":
            entered_str = input("Please enter your password to encode: ")
            encoded_pass = encoder(entered_str)
            print("Your password has been encoded and stored!")
        if user_input == "2":
            print(f"The encoded password is {encoded_pass}, and the original password is {entered_str}")
        if user_input == "3":
            quit()
