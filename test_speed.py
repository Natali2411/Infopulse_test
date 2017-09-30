speed = input("Enter speed: ")
speed = int(speed)

if speed >= 70 and speed <= 140:
    print("You are so busted!")
elif speed > 140:
    print("Your speed are unavailable")
elif speed < 70 and speed > 0:
    print("Have a nice day!")
elif speed < 0:
    print("You entered a negative value")