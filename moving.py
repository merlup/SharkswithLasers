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

# MultiDimensional Array

Field = [[B1_A,B1_B],[B2_A,B2_B],[B3_A],[R3_A],[R2_A,R2_B],[R1_A,R1_B]]


#Find Index of Element in MultiDimenstional Array
def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
            return row, column
        except ValueError:
                return row, column
        return -1

print(find(Field, B1_A)) #Returns (0,0) Correct
print(find(Field, B1_B)) #Returns (0,1) Correct
#print(find(Field, B2_B)) #Throws Error

# Set a Servo Status Active
B1_B.status ="Active"

def MoveUp():

        #Iterate through each item in Field
        for i in Field:
                #if item status equal to Active
                if i.status == "Active":
                        #if item index 3 item in the multidimensional array
                        if find(Field, i) == (2,0):
                        #current position is this index
                          current_position = (find(Field, i))
                          print(current_position)
                          #new position is this index + 1
                          new_position = current_position + 1
                          #old position if new position - 1
                          old_position = new_position - 1
                          #Set the servos status in the new postion to Active
                          Field(new_position).status = "Active"
                          #Set the servos status in the old position to UnActive
                          Field(old_position).status = "UnActive"

                        else:
                           #current position is this index
                           current_position = (find(Field, i))
                           #new position is this index + 2
                           new_position = current_position + 2
                           #old position if new position - 2
                           old_position = new_position - 2
                           #Set the servos status in the new postion to Active
                           Field(new_position).status = "Active"
                           #Set the servos status in the old position to UnActive
                           Field(old_position).status = "UnActive"

MoveUp()

