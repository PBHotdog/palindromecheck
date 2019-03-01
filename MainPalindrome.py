# Start of the top of the program, hello!


'''
check_palindrome checks to see if the word, inverted, is equal to the word regularly
[::-1] is using a slice to check the inverted word
'''


def check_palindrome(user_input):
    if str(user_input) == str(user_input)[::-1]:
        print("Congrats! (" + user_input + ") is indeed a palindrome!")
        return True
    else:
        print("Turns out (" + user_input + ") isn't a palindrome. Try again!")
        return False


'''
MAIN STARTS HERE:
Starts off with a while function this loops the program if the word isn't a palindrome 
After that, a print function is asking user for input
At the start of the if statement, checks to see if the user input contains only alphabetical characters
if so goes along the else statement
'''
is_running = True
while is_running is True:
    print("Hello, please enter a word you would like to check")
    user_input = input()
    if user_input.isalpha():
        print("Ok! Your word (" + user_input + ") is in fact a word! Let's check it now")
        if check_palindrome(user_input) is True:
            is_running = False
        else:
            is_running = True
    else:
        print("Hey! You gotta input a word!")


