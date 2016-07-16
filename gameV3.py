
#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
from Adafruit_PWM_Servo_Driver import PWM
import pygame
import time
import atexit
from time import sleep
import threading


#### Initialize Pygame

pygame.joystick.init()
#joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
pygame.init()


for i in range(0, pygame.joystick.get_count()):
	joysticks.append(pygame.joystick.Joystick(1))
	joysticks(-1).init()
	print("Detected joystick: " + joysticks[-1].get_name())

#Create Threads Object for Running motors at the same time
st1 = threading.Thread()
st2 = threading.Thread()

def stepper_worker(stepper, numsteps, direction, style):
	stepper.step(numsteps, direction, style)
######
# Classes and Methods
class Servo:
	
	def SetName(self, name):
		self.name = name
		
	def SetOwner(self,name):
		self.controlled_by = name
		
	def SetLED(self, name):
		self.led = name
	
	def SetPosition(self, position):
		self.posiion = position
		
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
PlayerBlueStepper = MotorHat.getStepper(100, 1)       # 200 steps/rev, motor port #1
PlayerBlueStepper.setSpeed(30)                  # 30 RPM
PlayerRedStepper = MotorHat.getStepper(100, 1)
PlayerRedStepper.setSpeed(30)

#Moving Motor
def MoveBlueSharkLeft():
	PlayerBlueStepper.step(1, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
	print("Moving Left")
def MoveBlueSharkRight():
	print("Moving right")
	PlayerBlueStepper.step(1, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
def BlueSharkStop():
	turnOffMotors()
def RedSharkStop():
	turnOffMotors()
#PlayerBlueStepper.step(0, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
def MoveBlueSharkRightSlowed():
	print("Moving Right Slowed")	
	PlayerBlueStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

def MoveBlueSharkLeftSlowed():
	print("Moving Left Slowed")	
	PlayerBlueStepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
def MoveRedSharkLeft():
	print("Red Shark Left")
	PlayerRedStepper.step(1, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
def MoveRedSharkRight():
	print("Red Shark Right")
	PlayerRedStepper.step(1, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)

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

# Initialize Servo Values
Blue_Servo_Row_1_A=Servo()
Blue_Servo_Row_1_A.SetName("B_R1_A")
Blue_Servo_Row_1_A.SetOwner("Open")
Blue_Servo_Row_1_A.SetLED("Off")

Blue_Servo_Row_1_B=Servo()
Blue_Servo_Row_1_B.SetName("B_R1_B")
Blue_Servo_Row_1_B.SetOwner("Open")
Blue_Servo_Row_1_B.SetLED("Off")

Blue_Servo_Row_2_A=Servo()
Blue_Servo_Row_2_A.SetName("B_R2_A")
Blue_Servo_Row_2_A.SetOwner("Open")
Blue_Servo_Row_2_A.SetLED("Off")

Blue_Servo_Row_2_B=Servo()
Blue_Servo_Row_2_B.SetName("B_R2_B")
Blue_Servo_Row_2_B.SetOwner("Open")
Blue_Servo_Row_2_B.SetLED("Off")

Blue_Servo_Row_3_A=Servo()
Blue_Servo_Row_3_A.SetName("B_R3_A")
Blue_Servo_Row_3_A.SetOwner("Open")
Blue_Servo_Row_3_A.SetLED("Off")


Red_Servo_Row_1_A=Servo()
Red_Servo_Row_1_A.SetName("R_R1_A")
Red_Servo_Row_1_A.SetOwner("Open")
Red_Servo_Row_1_A.SetLED("Off")


Red_Servo_Row_1_B=Servo()
Red_Servo_Row_1_B.SetName("R_R1_B")
Red_Servo_Row_1_B.SetOwner("Open")
Red_Servo_Row_1_B.SetLED("Off")

Red_Servo_Row_2_A=Servo()
Red_Servo_Row_2_A.SetName("R_R2_A")
Red_Servo_Row_2_A.SetOwner("Open")
Red_Servo_Row_2_A.SetLED("Off")

Red_Servo_Row_2_B=Servo()
Red_Servo_Row_2_B.SetName("R_R2_B")
Red_Servo_Row_2_B.SetOwner("Open")
Red_Servo_Row_2_B.SetLED("Off")

Red_Servo_Row_3_A=Servo()
Red_Servo_Row_3_A.SetName("R_R3_A")
Red_Servo_Row_3_A.SetOwner("Open")
Red_Servo_Row_3_A.SetLED("Off")

# Initialize Player Values 	
Player_Blue=Player()
Player_Blue.PlayerName("Blue")
Player_Blue.PlayerHealth(100)
Player_Blue.PlayerLives(3)

Player_Red=Player()
Player_Red.PlayerName("Red")
Player_Red.PlayerHealth(100)
Player_Red.PlayerLives(3)

#Array of Servos

Blue_Side = [
	Blue_Servo_Row_1_A,
	Blue_Servo_Row_1_B,
	Blue_Servo_Row_2_A,
	Blue_Servo_Row_2_B,
	Blue_Servo_Row_3_A
]

Red_Side = [
	Red_Servo_Row_1_A,
	Red_Servo_Row_1_B,
	Red_Servo_Row_2_A,
	Red_Servo_Row_2_B,
	Red_Servo_Row_3_A
]

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

def Defense_Blue():
		for servo in Blue_Side:
			if servo.controlled_by == "Red":
				ChangeServoNormal(servo)
				print("Defense")
			
def Defense_Red():
	for servo in Red_Side:
		if servo.controlled_by == "Blue":
			ChangeServoNormal(servo)
			print("Defense")

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
	
def Start_Blue_Attack():
#Wait 10 seconds before restoring power
	Restore_Red()	
	
def Start_Red_Attack():
#Wait 10 seconds before restoring power
	Restore_Blue()

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
 
if not st1.isAlive():
	st1 = threading.Thread(target=stepper_worker, args=(PlayerBlueStepper, 100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE))
st1.start()
if not st2.isAlive():
        st2 = threading.Thread(target=stepper_worker, args=(PlayerRedStepper, 100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE))
st2.start()

try:
	while True:
        	#if not st1.isAlive():
			#st1 = threading.Thread(target = stepper_worker, args=(PlayerBlueStepper, 100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE))
       		#st1.start()
        	#if not st2.isAlive():
			#st2 = threading.Thread(target = stepper_worker, args=(PlayerRedStepper, 100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE))
       		#st2.start()
       		pwm.setPWM(2, 2, servoMin)
		pwm.setPWM(3, 3, servoMin)
		pwm.setPWM(4, 4, servoMin)
  #	time.sleep(1)
  		pwm.setPWM(2, 2, servoMax)
		pwm.setPWM(3, 3, servoMax)
		pwm.setPWM(4, 4, servoMax)
  #	time.sleep(1)

		#for event in pygame.event.get():
			#for stick in Sticks:
				#print("sticks=" + str(len(Sticks)))
				#axes = joysticks[0].get_numaxes()
				
				#for i in range(axes):	
                			#axis = joysticks[0].get_axis(0)
                			
                			#if axis < 0:
                        			#MoveBlueSharkRight()
					#if axis > 0:
						#MoveBlueSharkLeft()
					#if axis == 0:
						#BlueSharkStop()
				#axes2 = joysticks[1].get_numaxes()
				#for i in range(axes2):
					#axis2 = joysticks[1].get_axis(0)
					#if axis2 > 0:
						#print("Red")
						#MoveRedSharkLeft()
					#if axis2 < 0:
						#MoveRedSharkRight()
					#if axis2 == 0:
						#RedSharkStop()
finally: 
	print("End")
