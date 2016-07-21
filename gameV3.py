
#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor
from Adafruit_PWM_Servo_Driver import PWM
import RPi.GPIO as GPIO
import pygame
import time
import atexit
from time import sleep
import threading

# Setup GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#### Initialize Pygame

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

#Create Threads Object for Running motors at the same time
MotorThread1 = threading.Thread()
MotorThread2 = threading.Thread()

def stepper_worker(stepper, numsteps, direction, style):
	stepper.step(numsteps, direction, style)

# Classes

class Servo:
	
	def SetName(self, name):
		self.name = name
		
	def SetOwner(self,name):
		self.controlled_by = name
		
	def SetLED(self, name):
		self.led = name
	
	def SetPosition(self, position):
		self.posiion = position
	def SetStatus(self, status):
		self.status = status
		
class Player:
	
	def PlayerName(self, name):
		self.name = name
		
	def PlayerHealth(self, health):
		self.health = health
		
	def TakeDamage(self, damage):
		self.damage = damage
		self.health = self.health - damage
		
	def PlayerLives(self, lives):
		self.lives = 3
	
	def ResetHealth(self):
		self.health = 100
	
	def TakeLife(self):
			self.lives = self.lives - 1
			print("You lost a life")



# Setting the MotorHat I2C address
MotorHat = Adafruit_MotorHAT(addr = 0x60)

#Turn Off Motor On Exit
def turnOffMotors():
        MotorHat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        MotorHat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        MotorHat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        MotorHat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
atexit.register(turnOffMotors)


#Creating the Stepper Motor Object

PlayerBlueStepper = MotorHat.getStepper(50, 1)       
PlayerBlueStepper.setSpeed(200)                 
PlayerRedStepper = MotorHat.getStepper(10, 2)
PlayerRedStepper.setSpeed(100)

#Moving Motor
def MoveBlueSharkLeft():
	PlayerBlueStepper.step(15, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
        print("Blue Shark Left")
def MoveBlueSharkRight():
	print("Blue Shark right")
	PlayerBlueStepper.step(15, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
def BlueSharkStop():
	print("BlueNotMoving")
	#turnOffMotors()
def RedSharkStop():
	print("RedNotMoving")
	#turnOffMotors()
def MoveBlueSharkRightSlowed():
	print("Moving Right Slowed")	
	PlayerBlueStepper.step(10, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

def MoveBlueSharkLeftSlowed():
	print("Moving Left Slowed")	
	PlayerBlueStepper.step(10, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
def MoveRedSharkLeft():
	print("Red Shark Left")
	PlayerRedStepper.step(10, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
	turnOffMotors()
def MoveRedSharkRight():
	print("Red Shark Right")
	PlayerRedStepper.step(50, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
	
# Initialise the PWM device using the default address
pwm = PWM(0x40)
servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 2, pulse)
  pwm.setPWM(channel, 3, pulse)
  pwm.setPWM(4, 4, pulse)

pwm.setPWMFreq(60)

# Initialize Servo Values

B1_A = Servo()
B1_A.SetName("B_R1_A")
B1_A.SetOwner("Open")
B1_A.SetLED("Off")
B1_A.SetStatus("UnActive")

B1_B = Servo()
B1_B.SetName("B_R1_B")
B1_B.SetOwner("Open")
B1_B.SetLED("Off")
B1_B.SetStatus("UnActive")

B2_A = Servo()
B2_A.SetName("B_R2_A")
B2_A.SetOwner("Open")
B2_A.SetLED("Off")
B2_A.SetStatus("UnActive")

B2_B = Servo()
B2_B.SetName("R_R2_B")
B2_B.SetOwner("Open")
B2_B.SetLED("Off")
B2_B.SetStatus("UnActive")

B3_A = Servo()
B3_A.SetName("R_R3_A")
B3_A.SetOwner("Open")
B3_A.SetLED("Off")
B3_A.SetStatus("UnActive")

R1_A = Servo()
R1_A.SetName("R_R1_A")
R1_A.SetOwner("Open")
R1_A.SetLED("Off")
R1_A.SetStatus("UnActive")

R1_B = Servo()
R1_B.SetName("R_R1_B")
R1_B.SetOwner("Open")
R1_B.SetLED("Off")
R1_B.SetStatus("UnActive")

R2_A = Servo()
R2_A.SetName("R_R2_A")
R2_A.SetOwner("Open")
R2_A.SetLED("Off")
R2_A.SetStatus("UnActive")

R2_B = Servo()
R2_B.SetName("R_R2_B")
R2_B.SetOwner("Open")
R2_B.SetLED("Off")
R2_B.SetStatus("UnActive")

R3_A = Servo()
R3_A.SetName("R_R3_A")
R3_A.SetOwner("Open")
R3_A.SetLED("Off")
R3_A.SetStatus("UnActive")

# Create Lights for Red , Blue, and Open for each servo

#Blue_Row_1A
L_B1_A = 14
L_R1_A = 4 
L_01_A = 17

GPIO.setup(L_B1_A, GPIO.OUT)
GPIO.setup(L_R1_A, GPIO.OUT)
GPIO.setup(L_01_A, GPIO.OUT)

#Blue_Row_1B
L_B1_B = 18
L_R1_B = 27
L_01_B = 22

GPIO.setup(L_B1_B, GPIO.OUT)
GPIO.setup(L_R1_B, GPIO.OUT)
GPIO.setup(L_01_B, GPIO.OUT)

#Blue_Row_2A
L_B2_A = 23
L_R2_A = 24
L_02_A = 25

GPIO.setup(L_B2_A, GPIO.OUT)
GPIO.setup(L_R2_A, GPIO.OUT)
GPIO.setup(L_02_A, GPIO.OUT)

#Blue_Row_2B
L_B2_B = 10
L_R2_B = 9
L_02_B = 11

GPIO.setup(L_B2_B, GPIO.OUT)
GPIO.setup(L_R2_B, GPIO.OUT)
GPIO.setup(L_02_B, GPIO.OUT)

#Blue_Row_3A
L_B3_A = 8
L_R3_A = 7
L_03_A = 5

GPIO.setup(L_B3_A, GPIO.OUT)
GPIO.setup(L_R3_A, GPIO.OUT)
GPIO.setup(L_03_A, GPIO.OUT)

#Red_Row_3A
L_03_AR =5
L_02_AR = 5
L_02_BR = 5
L_01_AR = 5
L_01_BR =5

Field = [B1_A, B1_B, B2_A, B2_B, B3_A, R3_A, R2_A, R2_B, R1_A, R1_B]
LED_Field = [L_B1_A, L_B1_B, L_B2_A, L_B2_B, L_B3_A, L_R3_A, L_R2_A,L_R2_B, L_R1_A, L_R1_B]
LED_Open = [L_01_A, L_01_B, L_02_A, L_02_B, L_03_A, L_03_AR, L_02_AR, L_02_BR, L_01_AR, L_01_BR]

# Set a Square Status Active


def MoveUp():
        for i in Field:
                if i.status == "Active":
                        if Field.index(i) == 4:
                          current_position = Field.index(i)
                          
                          new_position = current_position + 1
                          #print(new_position)
                          old_position = new_position - 1
                          #print(old_position)
                          Field[new_position].status = "Active"
                          Field[old_position].status = "UnActive"
                          return
                        elif Field.index(i) == 9:
				current_position = Field.index(i)
				new_position = current_position + 0
				old_position = current_position
				Field[old_position].status = "Active"
				return
			else:
                          current_position = Field.index(i)
                          #print(current_position)
                          new_position = current_position + 2
                          #print(new_position)
                          old_position = new_position - 2
                          #print(old_position)
                          Field[new_position].status = "Active"
                          Field[old_position].status = "UnActive"
                          return
def MoveDown():
        for i in Field:
                if i.status == "Active":
                        if Field.index(i) == 4:
                          current_position = Field.index(i)
                          #print(current_position)
                          new_position = current_position - 1
                          #print(new_position)
                          old_position = new_position + 1
                          #print(old_position)
                          Field[new_position].status = "Active"
                          Field[old_position].status = "UnActive"
                          return
                        elif Field.index(i) == 0:
				current_position = Field.index(i)
				new_position = current_position 
				old_position = new_position
				Field[new_position].status = "Active"
				return
			elif Field.index(i) == 1:
                                current_position = Field.index(i)
                                new_position = current_position - 1
                                old_position = new_position + 1
                                Field[new_position].status = "Active"
                                Field[old_position].status = "UnActive"
                        else:
                          current_position = Field.index(i)
                          #print(current_position)
                          new_position = current_position - 2
                          #print(new_position)
                          old_position = new_position + 2
                          #print(old_position)
                          Field[new_position].status = "Active"
                          Field[old_position].status = "UnActive"
                          return
def MoveLeft():
        for i in Field:
                if i.status == "Active":
                        if Field.index(i) == 0:
                                current_position = Field.index(i)
                                new_position = current_position - 0
                                old_position = current_position
                                Field[old_position].status = "Active"
                                return
                        else:
                                current_position = Field.index(i)
                                #print(current_position)
                                new_position = current_position - 1
                                #print(new_position)
                                old_position = new_position +1
                                #print(old_position)
                                Field[new_position].status = "Active"
                              	Field[old_position].status = "UnActive"
                                return
def MoveRight():
        for i in Field:
                if i.status == "Active":
                        if Field.index(i) == 9:
                                current_position = Field.index(i)
                                new_position = current_position + 0
                                old_position = current_position
                                Field[old_position].status = "Active"
                                return
                        else:
                                current_position = Field.index(i)
                                #print(current_position)
                                new_position = current_position + 1
                                #print(new_position)
                                old_position = new_position - 1
                                #print(old_position)
                                Field[new_position].status = "Active"
                                Field[old_position].status = "UnActive"
                                return

# Initialize Player Values 	
Player_Blue=Player()
Player_Blue.PlayerName("Blue")
Player_Blue.PlayerHealth(100)
Player_Blue.PlayerLives(3)

Player_Red=Player()
Player_Red.PlayerName("Red")
Player_Red.PlayerHealth(100)
Player_Red.PlayerLives(3)



# Timers and Sensors
Blue_Attack_Timer = range(10)
Red_Attack_Timer = range(10)
Blue_Attack_Sensor = "Low"
Red_Attack_Sensor = "Low"
Blue_Defense_Sensor = "Low"
Red_Defense_Sensor = "Low"
Blue_Target_Sensor = "Low"
Red_Target_Sensor = "Low"

# Game Logic		
def ChangeControll(Servo, Player):
	Servo.SetOwner(Player.name)
	Servo.SetLED(Player.name)	
def ChangeServoNormal(Servo):
	Servo.SetOwner("Open")
	Servo.SetLED("Open")


def Restore_Blue():
	for servo in Blue_Side:
		if servo.controlled_by == "Red":
			ChangeServoNormal(servo)
			print("Restored")
	
def Restore_Red():
	for servo in Red_Side:
		if servo.controlled_by == "Blue":
			ChangeServoNormal(servo)
			print("Restored")
def Defense_Blue():
		for servo in Blue_Side:
			if servo.controlled_by == "Red":
				ChangeServoNormal(servo)
				print("Defense")
				Restore_Blue()
			
def Defense_Red():
	for servo in Red_Side:
		if servo.controlled_by == "Blue":
			ChangeServoNormal(servo)
			print("Defense")
			Restore_Red()

def Attack_Blue():
	for servo in Red_Side:
		if servo.controlled_by == "Open" and servo.name == "R_R2_A" or servo.controlled_by == "Open" and servo.name == "R_R2_B":
			servo.controlled_by = "Blue"
		elif servo.controlled_by == "Red" and servo.name == "R_R2_A" or servo.controlled_by == "Open" and servo.name == "R_R2_B":
			servo.controlled_by = "Open"
	Start_Blue_Attack()
			
def Attack_Red():
	for servo in Blue_Side:
		if servo.controlled_by == "Open" and servo.name == "B_R2_A" or servo.controlled_by == "Open" and servo.name == "B_R2_B":
			servo.controlled_by = "Red"
		elif servo.controlled_by == "Blue" and servo.name == "B_R2_A" or servo.controlled_by == "Open" and servo.name == "B_R2_B":
			servo.controlled_by = "Open"
		Start_Red_Attack()
	
if Player_Blue.health == 0:
	print("Blue Shark has been Killed")
	Player_Blue.TakeLife()
	print(Player_Blue.lives)
	Player_Blue.ResetHealth()

if Player_Red.health == 0:
	print("Red Shark has been Killed")
	Player_Red.TakeLife()
	print(Player_Red.lives)
	Player_Red.ResetHealth()

if Blue_Attack_Sensor == "High":
	Attack_Blue()

if Red_Attack_Sensor == "High":
	Attack_Red()

if Blue_Defense_Sensor == "High":
	Defense_Blue()

if Red_Defense_Sensor == "High":
	Defense_Red()

if Blue_Target_Sensor == "High":
	Player_Red.TakeDamage(1)	

if Red_Target_Sensor == "High":
	Player_Blue.TakeDamage(1)

B1_A.status = "Active"
while True:
        
        
        #for i in Field:
                #if i.status == "Active":
                        #i.SetLED("On")
                        #print('one' %i)
                #else:
                        #i.SetLED("Off")
        #for i in Field:
               # position = Field.index(i)
                #if i.led == "On":
                        #print( Field.index(i))
                        #light_up = Field.index(i)
                        #print(light_up ("3"))
                        
                        #print(led_on ("4"))
                        #if light_up > 4:
                                #print("Not in Circuit")
                        #else:
                                #GPIO.output(LED_Field[light_up],False)
                #else:
                        #GPIO.output(LED_Open[position],True)
        #for i in Field:
                #i.led == "Off"
        #GPIO.cleanup()
        #GPIO.output(L_R1_A,True)
        GPIO.output(L_R2_A, True)
        GPIO.output(L_R2_B, True)
        #GPIO.output(L_R3_A, True)
        #Start Threads 
	if not MotorThread1.isAlive():
		MotorThread1 = threading.Thread(target = stepper_worker, args=(PlayerBlueStepper, 0, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE))
       		MotorThread1.start()
	if not MotorThread2.isAlive():
                MotorThread2 = threading.Thread(target = stepper_worker, args=(PlayerRedStepper, 0, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE))
       		MotorThread2.start()

       	#Start Watching Events	
	for event in pygame.event.get():
		joystick_count = pygame.joystick.get_count()

	#Initialize Controllers
	bluestick = pygame.joystick.Joystick(0)
	#bluebuttons = pygame.joystick.Joystick(0).get_numbuttons
        bluestick.init() 
	#Bluea = bluestick.get_button(0)
	
		
	redstick = pygame.joystick.Joystick(1)
	redstick.init()
		
	axes = bluestick.get_numaxes()
	axes2 = redstick.get_numaxes()	
	for i in range(axes):	
               	horizontal = bluestick.get_axis(0)
		vertical = bluestick.get_axis(1)
			
               	if horizontal < 0:
                        MoveRight()
                       	MoveBlueSharkRight()
                       	for i in Field:
                                if i.status == "Active":
                                        print(Field.index(i))
		if horizontal > 0:
			MoveLeft()
			MoveBlueSharkLeft()
			for i in Field:
                                if i.status == "Active":
                                        print(Field.index(i))
		if horizontal or vertical == 0:
			BlueSharkStop()
			for i in Field:
                                if i.status == "Active":
                                        print(Field.index(i))
                                 

		if vertical > 0:
			MoveUp()
			print("Up")
			for i in Field:
                                if i.status == "Active":
                                        print(Field.index(i))
		if vertical < 0:
			MoveDown()
			print("Down")
			for i in Field:
                                if i.status == "Active":
                                        print(Field.index(i))
	#if event.type == pygame.JOYBUTTONDOWN:
                #print("Blue Button")
	for i in range(axes2):
		axis2 = joysticks[1].get_axis(0)
		if axis2 > 0:
			MoveRedSharkLeft()
		if axis2 < 0:
			MoveRedSharkRight()
		if axis2 == 0:
			RedSharkStop()
			print("Stopped")
MoveUp()
MoveUp()
GPIO.cleanup()
for i in Field:
        i.status == "Unactive"
