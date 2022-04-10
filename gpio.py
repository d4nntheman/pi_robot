import time
import RPi.GPIO as GPIO

in0_1 = 5
in0_2 = 6
in1_1 = 13
in1_2 = 19
pwm_pin_id = 25

duty_cycle = 100

GPIO.setwarnings(False)                 #disable warnings
GPIO.setmode(GPIO.BCM)          #set pin numbering system

GPIO.setup(in0_1, GPIO.OUT)
GPIO.setup(in0_2, GPIO.OUT)
GPIO.output(in0_1, GPIO.LOW) # Turn LED on
GPIO.output(in0_2, GPIO.LOW) # Turn LED on

GPIO.setup(in1_1, GPIO.OUT)
GPIO.setup(in1_2, GPIO.OUT)
GPIO.output(in1_1, GPIO.LOW) # Turn LED on
GPIO.output(in1_2, GPIO.LOW) # Turn LED on

GPIO.setup(pwm_pin_id, GPIO.OUT)
pi_pwm = GPIO.PWM(pwm_pin_id, 50)               #create PWM instance with frequency
pi_pwm.start(0)                         #start PWM of required Duty Cycle
pi_pwm.ChangeDutyCycle(0) #provide duty cycle in the range 0-100

def incrementing():
    time.sleep(1.5)
    max_duty = 90
    while True:
        GPIO.output(in1, GPIO.HIGH) # Turn LED on
        GPIO.output(in2, GPIO.LOW) # Turn LED on

        for duty in range(0,max_duty + 1,1):
            print(duty)
            pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
            time.sleep(0.1)
        time.sleep(1.5)

        for duty in range(max_duty,-1,-1):
            print(duty)
            pi_pwm.ChangeDutyCycle(duty)
            time.sleep(0.1)

        time.sleep(1.5)

        #GPIO.output(in1, GPIO.LOW)  # Turn LED off
        GPIO.output(in1, GPIO.LOW) # Turn LED on
        GPIO.output(in2, GPIO.LOW) # Turn LED on
        time.sleep(2)                   # Delay for 1 second

def backwards():
    GPIO.output(in0_1, GPIO.LOW) # Turn LED on
    GPIO.output(in0_2, GPIO.HIGH) # Turn LED on
    GPIO.output(in1_1, GPIO.LOW) # Turn LED on
    GPIO.output(in1_2, GPIO.HIGH) # Turn LED on

    pi_pwm.ChangeDutyCycle(duty_cycle) #provide duty cycle in the range 0-100

def backwards_for_n_seconds(n):
    backwards()
    time.sleep(n)
    stop()

def forward():
    GPIO.output(in0_1, GPIO.HIGH) # Turn LED on
    GPIO.output(in0_2, GPIO.LOW) # Turn LED on
    GPIO.output(in1_1, GPIO.HIGH) # Turn LED on
    GPIO.output(in1_2, GPIO.LOW) # Turn LED on

    pi_pwm.ChangeDutyCycle(duty_cycle) #provide duty cycle in the range 0-100

def forward_for_n_seconds(n):
    forward()
    time.sleep(n)
    stop()

def left():
    GPIO.output(in0_1, GPIO.LOW) # Turn LED on
    GPIO.output(in0_2, GPIO.HIGH) # Turn LED on
    GPIO.output(in1_1, GPIO.HIGH) # Turn LED on
    GPIO.output(in1_2, GPIO.LOW) # Turn LED on
    pi_pwm.ChangeDutyCycle(duty_cycle) #provide duty cycle in the range 0-100


def left_for_n_seconds(n):
    left()
    time.sleep(n)
    stop()


def right():
    GPIO.output(in0_1, GPIO.HIGH) # Turn LED on
    GPIO.output(in0_2, GPIO.LOW) # Turn LED on
    GPIO.output(in1_1, GPIO.LOW) # Turn LED on
    GPIO.output(in1_2, GPIO.HIGH) # Turn LED on

    pi_pwm.ChangeDutyCycle(duty_cycle) #provide duty cycle in the range 0-100

def right_for_n_seconds(n):
    right()
    time.sleep(n)
    stop()

def stop():
    pi_pwm.ChangeDutyCycle(0) #provide duty cycle in the range 0-100
    GPIO.output(in0_1, GPIO.LOW) # Turn LED on
    GPIO.output(in0_2, GPIO.LOW) # Turn LED on
    GPIO.output(in1_1, GPIO.LOW) # Turn LED on
    GPIO.output(in1_2, GPIO.LOW) # Turn LED on


