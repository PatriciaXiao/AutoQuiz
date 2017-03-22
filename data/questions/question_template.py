# abstract class
from abc import ABCMeta, abstractmethod, abstractproperty

class QuestionTemplate(object):

	__metaclass__ = ABCMeta

	# def __init__(self):
	#	#

	# abstract properties
	@abstractproperty
	def ID(self): pass

	# abstract methods
	@abstractmethod
	def math_model(self, input_list): pass # a blackbox of input map to output for a single calse of this question