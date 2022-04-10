import time
import RPi.GPIO as GPIO

in1 = 5
in2 = 6
pwm_pin_id = 25

GPIO.setwarnings(False)                 #disable warnings
GPIO.setmode(GPIO.BCM)          #set pin numbering system

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

GPIO.output(in1, GPIO.LOW) 
GPIO.output(in2, GPIO.LOW) 

GPIO.setup(pwm_pin_id, GPIO.OUT)
pi_pwm = GPIO.PWM(pwm_pin_id, 50)               #create PWM instance with frequency

pi_pwm.start(0)                         #start PWM of required Duty Cycle
pi_pwm.ChangeDutyCycle(0) #provide duty cycle in the range 0-100

