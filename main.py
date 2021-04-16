speed_limit = int(input("What was your speed limit of the road: "))
speed_allowed = int(input("what was the allowed speed of the road: "))
points = (speed_allowed - speed_limit)/5

if speed_limit < 60:
    print("OK")
else:
    if points < 12:
        print("Demerit points: " + str(points))
    else:
        print("Time to go to jail")

