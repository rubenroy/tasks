from os.path import exists
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
	filepath = ""
	def __init__(self,filepath):
		self.filepath=filepath
	#def __init__(self, newList):
	#	self.taskList = newListl
	
	def addTask(self,newTask):
		self.taskList.append(newTask)

	def listTasks(self):
		for task in self.taskList:
			if(task.done is False):
				print task.priority, task.description

	def saveTasks(self):
		
		pickleDump = open(self.filepath,'wb+')
		pickle.dump(self.taskList,pickleDump)
		pickleDump.flush()
		pickleDump.close()

	def loadTasks(self):
		if exists(self.filepath):
			pickleLoad = open(self.filepath,'rb')
			self.taskList = pickle.load(pickleLoad)
			pickleLoad.close()	

# main()
import argparse,pickle



parser = argparse.ArgumentParser(description='A quick and dirty command-line todo-list manager')
parser.add_argument('-a','--add', help='add todo item', required=False)
parser.add_argument('-l','--list', help='list all tasks', required=False, action = "store_true")
parser.add_argument('-v','--verbose', help='verbose output', required=False, action = "store_true")
parser.add_argument('-f','--file', help='specify file', required=False)
args = vars(parser.parse_args())

filepath = "todo.lst"
if args['file'] is not None:
	filepath = args['file']

TM = TaskManager(filepath)
TM.loadTasks()
if args['add'] is not None:
	TM.addTask(Task(args['add']))
	if args['verbose']:
		print "Added task:", args['add']

if (args['list']):
	TM.listTasks()


TM.saveTasks()
#TM.listTasks()








