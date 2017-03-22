from __init__ import *
from functions import *

#@app.route('/')
@app.route('/', methods=['GET','POST'])
def question():
	question_id = 1
	question_parameter = 100
	answer_expected, cand_list = generate_cand_list(dec2bin, question_parameter, \
		interval=4, amount=5, limit=True, lim_min = 0, lim_max=2*question_parameter)
	session['cand_list'] = cand_list
	session['answer_expected'] = answer_expected
	session['question_parameter'] = question_parameter
	session['question_id'] = question_id
	'''
	if request.method == 'POST':
		# print "answer got {0}".format(request.form['candidate'])
		if request.form['candidate'] == answer_expected:
			print "correct answer"
		else:
			print ["wrong answer", request.form['candidate'], "supposed to be {0}={1}".format(question_parameter, answer_expected)]
		return redirect(url_for('report_result', \
			question_id=question_id, \
			question_parameter = question_parameter, \
			selected=request.form['candidate']))
		# called by question_id = request.args['question_id'] #session['messages']
		# 	cand_list = session['cand_list']
		# 	selected = request.args['selected']
		# 	question_parameter = request.args['question_parameter']
		# in function report_result
	'''
		
	return render_template('single_question_layout.html', \
		question_id = question_id, \
		question_parameter = question_parameter, \
		cand_list=cand_list)

@app.route('/result', methods=['GET', 'POST'])
def report_result():
	question_id = session['question_id']
	cand_list = session['cand_list']
	answer_expected = session['answer_expected']
	question_parameter = session['question_parameter']
	selected = request.form['candidate']
	return render_template('single_result_layout.html', \
		question_id = question_id, \
		question_parameter = question_parameter, \
		selected = selected, \
		cand_list = cand_list )



if __name__ == '__main__':
	app.run()