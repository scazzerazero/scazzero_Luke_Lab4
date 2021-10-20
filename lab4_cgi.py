#!/usr/bin/python37all

#put this file in /usr/lib/cgi-bi and change permissions (sudo chmod 755 led.py)
    #for cgi code to be executable we must make it executable by anyone. Chmod changes permissions on files. Gives anyone read and execute permissions.

import RPi.GPIO as GPIO
import cgi
import cgitb #for exception handling
cgitb.enable()

GPIO.setmode(GPIO.BCM) # for Pis pin numbering convention
GPIO.setwarning(False) # ignore warnigns due to multiple scripts at same time
BlPin=20
RdPin=21
GrPin=26

#begin generation of wen page showing current state:

print('Content-type:text/html\n\n <!-- every print line will now be interp as html-->')
print('<html>')
print('<head><title>LED SWITCH</title></head>')
print('<body style="background-color:lightblue;">')
print('<h3>Which LED you want?</h3>')
print('<form action="/cgi-bin/radio.py" method="POST";text-align:center>)
print(' <input type="radio" name="LEDoption" value="LED1" checked> Blue <br>')
print(' <input type="radio" name="LEDoption" value="LED2" checked> Green<br>')
print(' <input type="radio" name="LEDoption" value="LED3" checked> Red <br>')
print(' <input type="submit" value="Submit LED Selection">')
print('</form>')
print('<h3>What Brightness you want?</h3>')
print(' <form action="/cgi-bin/range.py" method="POST">')
print('   <input type="range" name="slider1" min="0" max="100" value="50"/><br>')
print('   <input type="submit" value="Submit Brightness Value">')
form =cgi.FieldStorage() #returns data passed to a CGI script as a FieldStorage object (similar to a Python dictionary)
if (form.getvalue('LEDoption') =="LED1"):
  GPIO.output(BlPin,1)
  GPIO.output(GrPin,0)
  GPIO.output(RdPin,0)
elif(form.getvalue('LEDoption') =="LED2"):
  GPIO.output(BlPin,0)
  GPIO.output(GrPin,1)
  GPIO.output(RdPin,0)
elif(form.getvalue('LEDoption') =="LED3"):
  GPIO.output(BlPin,0)
  GPIO.output(GrPin,0)
  GPIO.output(RdPin,1)






