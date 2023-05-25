import time
import random
import threading
flag=1
point=1
max=5

    
def countdown_timer():
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("Go!\a")
    
def score():
    point=point+1
    print("Score: "+point)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetset2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYqwertyuiopasdfghjklzxcvbnm'
alphabetset3 = 'ABCDEFGHIJKLMNOP1234567890!@#$%^&*()-=+{]}:"<>?/qwertyuiopasdfghijklmnbvcxz'   
print("Welcome to TYPING MASTER!")
name=input("Name: ")
print("Hello,"+ name+"\n\nWe hope you are ready to face this challenge!\nType the letter the moment you see it!\n\n")
countdown_timer()
while(flag == 1):
    random_letter=random.choice(alphabet)
    print("Letter: "+random_letter)
    def get_user_input():
        global user_input
        user_input = input("Input: ")
    input_thread = threading.Thread(target=get_user_input)
    input_thread.start()
# Wait for 5 seconds
    input_thread.join(timeout=max)
# Check if the input thread is still alive
    if input_thread.is_alive():
        print("Timeout")
        print("POINTS: ",point)
        exit(0)
        input_thread.join()
        exit
    if(random_letter==user_input):
        {
        point:=point+1
        }
    if(random_letter!=user_input):
        flag = 0
        print(point)
        exit
if(point>10 & point<20):
    max=3
if(point>20 & point<30):
    max=2
if(point>30):
    max=1
    
