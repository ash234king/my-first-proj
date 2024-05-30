import time

length_of_countdown=input("Enter the length of countdown in seconds : ")   #to take input of length of countdown in seconds


integral_length=int(length_of_countdown)          #to convert the string into an integer value


def countdown(t):                    #defining a function countdown
    while t:                              
        minutes,seconds=divmod(t,60)       # to convertthe given input in form of minutes, seconds
        e="{:02d}:{:02d}".format(minutes,seconds)
        print(e,end="\r")                #to force the cursor to go back to the start of the screen 
        time.sleep(1)      #to make the code wait for 1 second
        t-=1               #decrement of time so that loop can converge to t=0
    print("Fire in the hole")          # when the while loop ends Fire in the hole gets printed





countdown(integral_length)                 # to pass the input into the countdown function
