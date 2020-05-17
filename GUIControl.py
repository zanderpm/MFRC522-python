import Read
import Write
import Dump
import readwriteinterface
import RPi.GPIO as GPIO
from guizero import App, Text

GPIO.setwarnings(false)


def read():
try:
  block=int(app.question("Block", "Which block would you like to read?"))
  Read.read(block)


def write():
  readwriteinterface.write()
#Or
#Ask which block
#Open window with block in buttons you can click on then edit, and a button to write everything.

def dump():
  Dump.dump()

app = App()
prompt=Text(app, "What would you like to do?")
readbut=PushButton(app, command=read)
writebut=PushButton(app, command=write)
dumpbut=PushButton(app, command=dump)

app.display()
