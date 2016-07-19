class Square:
	
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
B1_A = Square()
B1_A.SetName("B_R1_A")
B1_A.SetOwner("Open")
B1_A.SetLED("Off")
B1_A.SetStatus("UnActive")

B1_B = Square()
B1_B.SetName("B_R1_B")
B1_B.SetOwner("Open")
B1_B.SetLED("Off")
B1_B.SetStatus("UnActive")

B2_A = Square()
B2_A.SetName("B_R2_A")
B2_A.SetOwner("Open")
B2_A.SetLED("Off")
B2_A.SetStatus("UnActive")

B2_B = Square()
B2_B.SetName("R_R2_B")
B2_B.SetOwner("Open")
B2_B.SetLED("Off")
B2_B.SetStatus("UnActive")

B3_A = Square()
B3_A.SetName("R_R3_A")
B3_A.SetOwner("Open")
B3_A.SetLED("Off")
B3_A.SetStatus("UnActive")

R1_A = Square()
R1_A.SetName("R_R1_A")
R1_A.SetOwner("Open")
R1_A.SetLED("Off")
R1_A.SetStatus("UnActive")

R1_B = Square()
R1_B.SetName("R_R1_B")
R1_B.SetOwner("Open")
R1_B.SetLED("Off")
R1_B.SetStatus("UnActive")

R2_A = Square()
R2_A.SetName("R_R2_A")
R2_A.SetOwner("Open")
R2_A.SetLED("Off")
R2_A.SetStatus("UnActive")

R2_B = Square()
R2_B.SetName("R_R2_B")
R2_B.SetOwner("Open")
R2_B.SetLED("Off")
R2_B.SetStatus("UnActive")

R3_A = Square()
R3_A.SetName("R_R3_A")
R3_A.SetOwner("Open")
R3_A.SetLED("Off")
R3_A.SetStatus("UnActive")

# MultiDimensional Array

Field = [B1_A, B1_B, B2_A, B2_B, B3_A, R3_A, R2_A, R2_B, R1_A, R1_B]


#Find Index of Element in MultiDimenstional Array
#def find(l, elem):
    #for row, i in enumerate(l):
        #try:
            #column = i.index(elem)
            #return row, column
        #except ValueError:
                #return row, column
        #return -1

#print(find(Field, B1_A)) #Returns (0,0) Correct
#print(find(Field, B1_B)) #Returns (0,1) Correct
#print(find(Field, B2_B)) #Throws Error

# Set a Square Status Active
B1_A.status ="Active"

def MoveUp():
        for i in Field:
                if i.status == "Active":
                        if Field.index(i) == 4:
                          current_position = Field.index(i)
                          print(current_position)
                          new_position = current_position + 1
                          print(new_position)
                          old_position = new_position - 1
                          print(old_position)
                          Field[new_position].status = "Active"
                          Field[old_position].status = "UnActive"
                          
                        else:
                          current_position = Field.index(i)
                          print(current_position)
                          new_position = current_position + 2
                          print(new_position)
                          old_position = new_position - 2
                          print(old_position)
                          Field[new_position].status = "Active"
                          Field[old_position].status = "UnActive"
                          return
def MoveDown():
        for i in Field:
                if i.status == "Active":
                        if Field.index(i) == 4:
                          current_position = Field.index(i)
                          print(current_position)
                          new_position = current_position - 1
                          print(new_position)
                          old_position = new_position + 1
                          print(old_position)
                          Field[new_position].status = "Active"
                          Field[old_position].status = "UnActive"
                          
                        else:
                          current_position = Field.index(i)
                          print(current_position)
                          new_position = current_position - 2
                          print(new_position)
                          old_position = new_position + 2
                          print(old_position)
                          Field[new_position].status = "Active"
                          Field[old_position].status = "UnActive"
                          return
def MoveLeft():
        for i in Field:
                if i.status == "Active":
                          current_position = Field.index(i)
                          print(current_position)
                          new_position = current_position - 1
                          print(new_position)
                          old_position = new_position +1
                          print(old_position)
                          Field[new_position].status = "Active"
                          Field[old_position].status = "UnActive"
                          return
def MoveRight():
        for i in Field:
                if i.status == "Active":
                          current_position = Field.index(i)
                          print(current_position)
                          new_position = current_position + 1
                          print(new_position)
                          old_position = new_position - 1
                          print(old_position)
                          Field[new_position].status = "Active"
                          Field[old_position].status = "UnActive"
                          return

MoveUp()
MoveUp()
MoveDown()
MoveDown()
MoveLeft()
MoveRight()
