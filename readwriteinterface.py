import Read
import Write
import Dump
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

continueRunning=True;
badBlocks=[0,1,2,3,7,11,15,19,23,27,31,35,39,43,47,51,55,59,63]

#shortcut for inputw
def inp(str):
    return raw_input(str)

#Returns true if 'block' is in 'badBlocks'
def isInBadBlocks(block):
    for x in badBlocks:
            if x==block:
                return True                
    return False

#User chose Read
def read():
    block=int(inp("What block would you like to read?"))
    print ("Reading...")
    print str(Read.read(block))
    



#User chose write
def write():
    # Get sector from user
    secOk=False
    while not secOk:
        #Get input
        try:
            sec=int(input("Which block would you like to edit? "))
        #Check that it's a number
        except:
            print ("You may have entered something that isn't a number. Please start over.")
            return
        #Check that it's in the right range
        if (not (sec>=0) or not (sec<=63)):
            print ("You have entered a number outside of the range. There are only 64 blocks on a 1K MIFARE card.")
            continue
        #Check that it's a writable block
        if (isInBadBlocks(sec)):
            print ("This block is not writable. Please try another block.")
        else:
            secOk=True
            
    # Get current data
    print ("Place card to see what is currently in block " + str(sec))  
                
    # Variable for the data to write
    data = Read.read(sec)

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
                    byteIn=int(inp("What goes in byte #" + str(task) + "?"))
                    if (byteIn>=0 and byteIn<=255):
                        data[task]=byteIn
                    else:
                        print ("Byte data must be between 0 and 255. Nothing has been written to this byte. Please try again.")
                else:
                    print ("There are only 16 bytes per block. Please start over, entering a number between 0 and 15, inclusive.")

            

    
    print ("Place card")
    #print str(data)
    Write.write(sec, data)
    print ("Written to block "+str(sec) + ":")
    print str(Read.read(sec))
    print ("\n")


#User chose Dump
def dump():
    print ("Place card")
    Dump.dump()


#User chose Clear
def clear():
    i=str(inp("You have chosen to erase the entire card. Are you absolutly sure that's what you want to do? ('y' for yes, 'n' for no)"))
    print ("Ok, if your sure...")
    print ("Place card")
    if (i=='y'):
        wipeArray=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for x in range(0, 64):
            if not (isInBadBlocks(x)):
                Write.write(x, wipeArray)
        print ("Done")
    else:
        print("Canceled.")


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

