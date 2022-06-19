def isPalindrome(text):
    rev = ''.join(reversed(text))

    if (text == rev):
        return True
    return False
 
# main function
text= input('enter a word: ')
answer = isPalindrome(text)
 
if (answer):
    print("Yes")
else:
    print("No")