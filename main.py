class Task:
	priority = 0
	description = ""
	done = False

	def __init__(self, description, priority = 0):
		self.priority = priority
		self.description = description
	
	def markDone(self):
		if(self.done != True):
			self.done = True
	
class TaskManager:
	taskList = list()

	#def __init__(self, newList):
	#	self.taskList = newList
	
	def addTask(self,newTask):
		self.taskList.append(newTask)

	def listTasks(self):
		for task in self.taskList:
			if(task.done is False):
				print task.priority, task.description

	def saveTasks(self):
		pickleDump = open("todo.lst",'wb')
		pickle.dump(self.taskList,pickleDump)
		pickleDump.flush()
		pickleDump.close()

	def loadTasks(self):
		pickleLoad = open("todo.lst",'rb')
		self.taskList = pickle.load(pickleLoad)
		pickleLoad.close()	

# main()
import sys,pickle
TM = TaskManager()
TM.loadTasks()

if(len(sys.argv)>1):
	if(sys.argv[1] == '-a'):
		TM.addTask(Task(sys.argv[2]))

for i in range(len(sys.argv)):
	if(sys.argv[i] == '-a'):
		TM.addTask( Task(sys.argv[i+1]) )
	elif (sys.argv[i] == '-l'):
		TM.listTasks()

TM.saveTasks()
#TM.listTasks()


