import machine
from machine import Pin
import time
import camera

flash = Pin(4, Pin.OUT)
flash.value(1)
time.sleep(1)
flash.value(0)

uos.mount(machine.SDCard(), "/sd")

camera.init(0, format=camera.JPEG) 
camera.quality(12)
camera.framesize(9)

count = 0

while True:
    if count == 2200 :
        flash.value(1)
        print("capture the images")
        break
    buf = camera.capture()
    file = open('/sd/'+str(count)+'.jpeg', 'w')
    file.write(buf)
    file.close()
    print(str(count)+'.jpeg is captured')
    
    count += 1
    time.sleep(1)
    
print("done all the work")