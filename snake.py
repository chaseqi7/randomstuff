import time
import copy
from random import randint
i=0
size=int(input('size:'))
textList=[]
while i<size:
	temp=[]
	j=0
	while j<size:
		temp.append("#")
		j+=1
	textList.append(temp)
	i+=1
position=[int(round(size/2, 0)),int(round(size/2, 0))]

listOfPositions=[]
global length
length=1
def generateFood(listOfPositions):
	food=[randint(0,size-1),randint(0,size-1)]
	while food in listOfPositions:
		food=[randint(0,size-1),randint(0,size-1)]
	return food
def anydup(thelist):
  seen=[]
  for x in thelist:
    if x in seen:
    	return True
    seen.append(x)
  return False

def refresh(textList,listOfPositions,food):
	
	temp=copy.deepcopy(textList)
	temp[food[0]][food[1]]="x"
	for pos in listOfPositions:
		temp[pos[0]][pos[1]]="O"
	return temp

t=0
food=generateFood(listOfPositions)
while t<1:
	listOfPositions.append([position[0],position[1]])
	if len(listOfPositions)>length:
		del listOfPositions[0]
	if anydup(listOfPositions):
		print("you're DEAD!")
		break
	if length==size*size:
		print("YOU WIN! YEEE")
		break
		

	if position==food:
		food=generateFood(listOfPositions)
		length+=1
	for i in range(0,size):
		print(refresh(textList,listOfPositions,food)[i])
	
	direction = input('')
	if direction=='w':
		position[0]-=1
	if direction=='a':
		position[1]-=1
	if direction=='s':
		position[0]+=1
	if direction=='d':
		position[1]+=1

	if position[0]>(size-1):
		position[0]=0
	if position[1]>(size-1):
		position[1]=0
	if position[0]<=-1:
		position[0]=(size-1)
	if position[1]<=-1:
		position[1]=(size-1)