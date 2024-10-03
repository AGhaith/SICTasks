from gpiozero import LED
from time import sleep
from datetime import datetime
import psutil
#green_led   = LED()         #insert pin for green led
#yellow_led  = LED()         #insert pin for yellow led
#red_led     = LED()         #insert pin for red led

def green():
    print("green")
 #  green_led.on()
 
def yellow():
    print("yellow")
 #  yellow_led.on()
 
def red():
    print("red")
 #  red_led.on()
 
 
Log = open("Log.txt",'w')
Log.close()
while True:
    
    Log = open("Log.txt",'a')
    
    cpu_usage = psutil.cpu_percent()
    
    status = f"{datetime.now().strftime('%Y-%B-%d\t%A %I:%M:%S %p')}\tThe Current Cpu Usage is {cpu_usage}%\n\n"
    
    Log.write(status)
    
    if (cpu_usage < 50 ) :
        
        green()
        
    elif (cpu_usage < 80 ) :
        
        yellow()
        
    else :
        
        red()
        
    Log.close()
    sleep(5)
    