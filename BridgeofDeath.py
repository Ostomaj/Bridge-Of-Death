print("STOP, Whoever cross the bridge of death must answer me these questions three.")
A=input("What is your name?")             #Variable holding answer to name question
#print(A)
B=input("What is your quest?")             #Variable holding answer to quest question
#print(B)
L = ["What is the air speed velocity of an unladen swallow?",
"What is your favorite color?",
"What is the capital of Assyria?"]  #List created with quetions to be randomly picked

#print(L[0])
import random as r                      #Random number Library
rn=r.randint(0,len(L)-1)                #Random number generated between 0 and 2

#print(rn)

C=input(L[rn])         #Randomly chosen from list created

if rn==0 and C.lower()=="african or european":           #Swallow
  print("What I don't know that! AHHHHHHHH!")
elif rn==1 and C.lower()=="blue":           #Favorite color
  print("Oh go right ahead!")
elif rn==2:              #Capital of Assyria?
  print("Death")
