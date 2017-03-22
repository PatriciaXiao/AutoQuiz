from question_template import *

class TestQuestion(QuestionTemplate):
	
	@property # it also works this way though : ID = 0
	def ID(self):
		return 0

	def math_model(self, input_list):
		for elem in input_list:
			print elem

question = TestQuestion()

# question.math_model([1, 2, 3])
print question.id