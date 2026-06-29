command =""
started = False
while command.lower() != "quit":
    command = input("> ").lower()
    if command == "start":
        if started: 
            print("car already started")
            continue
        else:
            started = True
        print("car started")

    elif command == "stop":
        if not started:
            print("car already stopped")
            continue
        else:
            started = False
        print("car stopped")
    
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit the game
        """)

    elif command == "quit":
        break

    else:
        print("I don't understand")

