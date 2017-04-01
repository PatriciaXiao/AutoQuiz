# abstract class
from abc import ABCMeta, abstractmethod, abstractproperty

class QuestionTemplate(object):

	__metaclass__ = ABCMeta

	# def __init__(self):
	#	#

	class input_standardized: #standardize the input
		@abstractmethod
		def __init__(self, raw_data_in): pass
		@abstractmethod
		def get(self): pass

	def set_input_data(self, raw_data_in):
		self.data = self.input_standardized(raw_data_in)
		return self.data.get()
	def get_input_data(self):
		return self.data.get()

	# abstract properties
	@abstractproperty
	def ID(self): pass				# the ID of the question
	# @abstractproperty
	# def data(self): pass


	# abstract methods
	@abstractmethod
	def math_model(self, data_in): pass # a blackbox of input map to output for a single calse of this question
	@abstractmethod
	def question(self, data_in): pass	# the question being asked generated from the input list