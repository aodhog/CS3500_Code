from random import randint 
import stop, time


def road():

    #opens file and initialises vairables. Must open as append as speed should already be in the road file
    i=0
    road = open("road.txt","a")
    letters=["U","L","D"]
    previous="L"
    angle=0

    #simulates road to 10,000 units
    cont=True
    while i<10000:
        if stop.Stop==True:
            i=10000
            break
        obstacle=[]
        choice=letters[randint(0,2)]
        current=randint(1,91)
        if choice=="L":
            previous=choice
            obstacle.append(choice)
            obstacle.append(0)
        elif (choice=="U" and previous=="D") or (choice=="D" and previous=="U"):
            True 
        elif choice==previous:
            previous=choice
            current=angle
            obstacle.append(choice)
            obstacle.append(current)
        else:
            previous=choice
            angle=current
            obstacle.append(choice)
            obstacle.append(current)
        if len(obstacle)>0:
            road.write(f"{obstacle[0]},")
            if obstacle[1]<=9:
                road.write(f"0{obstacle[1]}\n")
            else:
                road.write(f"{obstacle[1]}\n")
        i+=1
            
        
    road.close()
road()