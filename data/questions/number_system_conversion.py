from question_template import *

class NumSysConvert(QuestionTemplate):
	@property
	def ID(self):
		return 1
	def math_model(self, input_list):
		# input list in this case, consists of:
		# number, list