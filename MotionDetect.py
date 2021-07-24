import RPi.GPIO as GPIO
import time
import printstatus

time.sleep(5*60)      # wait for 5 minutes before monitoring
GPIO.setmode(GPIO.BCM)

PIR_Sensor=14                   # PIR sensor is connected to this pin
prev_status=0

GPIO.setup(PIR_Sensor,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
while(True):
    Motion=GPIO.input(PIR_Sensor)

    if prev_status==0 and Motion==1 :
        print('motion detected')
        import SendAlertMail
    elif Motion==1:
        print('Motion Sustains')
    else:
        print('No motion')
    prev_status=Motion
    time.sleep(1)


          


