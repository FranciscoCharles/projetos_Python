from PyQt5 import QtCore

'''

	version : 1.0.13112019
	
	informação:
	
		Este módulo implementa um manipulador de threads Qt. O
	objetivo é facilitar o uso desde a criação, execução e finalização
	de threads. Não há funções de sincronização no momento.
	
	information:
	
		This module implements a Qt thread handler. The goal is
	to make it easier to use since thread creation, execution and
	termination. There are no sync functions at this time.
	
'''

class QtThreadWorker(QtCore.QThread):
	
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
				
class QtThreadManager(object):
	'''
		This class handles Qt thread.
	'''
	def __init__(self, list_threads):
		if isinstance(list_threads,list):
			self.__threads = list_threads
			self.__name = 0
		else:
			raise TypeError('list_threads is not list object.')
			
	def __len__(self):
		return len(self.__threads)
		
	def countThreadRunning():
		count = 0
		for thread in self.__threads:
				if thread.isRunning():
					count += 1
		return count
		
	def addThread(self,target, args=None, name=None):
	
		if name is None:
			thread = ThreadExec(target=target, args=args, name='thread-'+str(self.__name))
		else:
			thread = ThreadExec(target=target, args=args, name=name)
			
		self.__threads.append(thread)
		self.__name += 1
		return thread
		
	def getThread(self, key):
	
		compare = None
		if isinstance(key,int):
			_len = len(self.__threads)
			if -_len <= key < _len:
				return self.__threads[key]
		elif isinstance(key,ThreadExec):
			compare = lambda _thread: _thread is key
		elif isinstance(key,str):
			compare = lambda _thread: _thread.name == key
			
		if compare is not None:
			for thread in self.__threads:
				if compare(thread):
					return thread
		return None
		
	def removeThread(self, key=None, all=False):
		if all == True:
			for thread in self.__threads:
				if thread.isRunning():
					thread.finished.disconnect()
					thread.terminate()
			self.__threads.clear()
		else:
			thread = self.getThread(key)
			if thread is not None:
				if thread.isRunning():
					thread.finished.disconnect()
					thread.terminate()
				self.__threads.remove(thread)