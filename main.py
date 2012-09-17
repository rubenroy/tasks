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
import argparse,pickle

TM = TaskManager()
TM.loadTasks()

parser = argparse.ArgumentParser(description='A quick and dirty command-line todo-list manager')
parser.add_argument('-a','--add', help='Add todo item', required=False)
parser.add_argument('-l','--list', help='List all tasks', required=False, action = "store_true")
parser.add_argument('-v','--verbose', help='Verbose output', required=False, action = "store_true")
args = vars(parser.parse_args())

if args['add'] is not None:
	TM.addTask(Task(args['add']))
	if args['verbose']:
		print "Added task:", args['add']

if (args['list']):
	TM.listTasks()


TM.saveTasks()
#TM.listTasks()








