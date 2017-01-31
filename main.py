def main():
    while True:
        again = raw_input("Would you like a new password? Enter y/n: ")

        if again == "n":
            print ("Goodbye!") #exits if user declines
            quit()
            
        elif again == "y":
            print ("Enjoy your new password! \nCheckout savedpassword.txt to view it.")
            return
        

if __name__ == "__main__":
    main()

import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print password
file_ = open('savedpassword.txt', 'w') #this saves the password overwriting the previous one
file_.write(password)
file_.write("\nSAVE THIS PASSWORD OR IT WILL BE OVERWRITTEN BY NEXT NEW PASSWORD")
file_.close()
