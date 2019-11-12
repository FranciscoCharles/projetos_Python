from PyQt5 import QtGui,QtCore

'''

	creation date : 26/10/2019
	version : 1.0.12112019-beta
	
	informação:
	
		Este módulo implementa um manipulador de threads Qt. O
	objetivo é facilitar o uso desde a criação, execução e finalização
	de threads. Não há funções de sincronização no momento.
	
	information:
	
		This module implements a Qt thread handler. The goal is
	to make it easier to use since thread creation, execution and
	termination. There are no sync functions at this time.
'''

class ThreadExec(QtCore.QThread):
	
	def __init__(self, target, args = None, name=''):
	
		QtCore.QThread.__init__(self)
		self.__name = name
		self.__target = target
		self.__args = args
		
	@property
	def name(self):
		return self.__name
		
	@name.setter
	def name(self, new_name):
		self.__name = new_name
		
	def run(self):
	
		if self.__args is None:
			self.__target()
		else:
			self.__target(*self.__args)
				
class ThreadManager(object):
	'''
		This class handles Qt thread.
	'''
	def __init__(self, list_threads):
	
		self.list_threads = list_threads
		self.__name = 0
		
	def addThread(self,target, args=None, name=None):
	
		if name is None:
			thread = ThreadExec(target=target, args=args, name='thread-'+str(self.__name))
		else:
			thread = ThreadExec(target=target, args=args, name=name)
			
		self.list_threads.append(thread)
		self.__name += 1
		
		return thread
		
	def removeAllThreads(self):
	
		for thread in self.list_threads:
			if thread.isRunning():
				thread.finished.disconnect()
				thread.terminate()
					
		self.list_threads.clear()
		
	def removeThreadName(self, name):
	
		for thread in self.list_threads:
			if thread.name == name:
				if thread.isRunning():
					thread.finished.disconnect()
					thread.terminate()
				self.list_threads.remove(thread)
				
	def removeThreadIndex(self, index):
	
		if self.list_threads[index].isRunning():
			self.list_threads[index].finished.disconnect()
			self.list_threads[index].terminate()
			
		self.list_threads.remove(index)
				
	def removeThread(self, current_thread):
	
		for thread in self.list_threads:
			if thread is current_thread:
				if thread.isRunning():
					thread.finished.disconnect()
					thread.terminate()
				self.list_threads.remove(thread)
				
	def getThreadName(self, name):
	
		for thread in self.list_threads:
			if thread.name == name:
				return thread
		return None
				
	def getThreadIndex(self, index):
		return self.list_threads[index]
		
	def getThread(self, current_thread):
	
		for thread in self.list_threads:
			if thread is current_thread:
				return thread
				
		return None	