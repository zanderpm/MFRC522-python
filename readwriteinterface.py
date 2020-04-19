import Read
import Write
import Dump
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

continueRunning=True;

#shortcut for input
def inp(str):
    return raw_input(str)

#User chose Read
def read():
    block=int(inp("What block would you like to read?"))
    print ("Reading...")
    Read.read(block)
    



#User chose write
def write():
    # Get sector from user
    sec=int(input("Which block would you like to edit? "))
    # Show current data
    #    print ("Place card to see what is currently in block " + str(sec))
    #    Read.read(sec)
    
                
    # Variable for the data to write
    data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    # Input Loop
    continueRunning=True
    while continueRunning:

        #Show updated data
        print (str(data))
        
    
        # Find out what to do next
        task=inp("Enter the byte number you wish to change, or enter 'a' for all, or 'd' for done.")

        # Process input
        if task=='d':
            continueRunning=False
            
        elif task=='a':
            # Fill the data with user input
            for x in range(0,16):
                data[x]=(input("What goes in byte #" + str(x) + "?"))

        else:
            try:
                task=int(task)
            except:
                print ("Command not recognized. Please try again.")
            else:
                if (task>=0 and task<=15):
                    data[task]=int(inp("What goes in byte #" + str(task) + "?"))
                else:
                    print ("There are only 16 bytes per block. Please start over, entering a number between 0 and 15, inclusive.")

            

    
    print ("Place card")
    Write.write(sec, data)
    print ("Written to block "+str(sec) + ":")
    Read.read(sec)
    print ("\n")


#User chose Dump
def dump():
    print ("Place card")
    Dump.dump()


#User chose Whipe
def clear():
    print("clear")



#Find out what the user wants to do
while continueRunning:
    task=inp("What would you like to do? (Read (r), Write (w), Dump (d), Clear (c), Exit(x))")


    if task == 'r':
        read()
    elif task =='w':
        write()
    elif task == 'd':
        dump()
    elif task == 'c':
        clear()
    elif task == 'x':
        continueRunning=False
    else:
        print("Command not recognized")
        #restart

