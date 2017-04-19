from question_template import *

class TestQuestion(QuestionTemplate):
	
	'''
	class input_standardized(object):
		def __init__(self, raw_data_in):
			self.mydata = raw_data_in
		def get(self):
			return self.mydata
	'''

	@property # it also works this way though : ID = 0
	def ID(self):
		return 0
	def question(self, input_list):
		for elem in input_list:
			print elem
	def math_model(self, input_list):
		for elem in input_list:
			print elem



question = TestQuestion()

# question.math_model([1, 2, 3])
print question.set_input_data(3)