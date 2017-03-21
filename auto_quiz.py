from __init__ import *
from functions import *

#@app.route('/')
@app.route('/', methods=['GET','POST'])
def question():
	question_id = 1
	question_parameter = 100
	answer_expected = dec2bin(question_parameter)
	dec_list = generate_cand_list(question_parameter, interval=4, amount=5, limit=True, lim_min = 0, lim_max=2*question_parameter)
	bin_list = list_dec2bin(dec_list)
	cand_list = random_order(bin_list)
	session['cand_list'] = cand_list
	'''
	# if update is needed
	session['to_update'] = True
	if session['to_update']:
		question_id = 1
		question_parameter = 100
		answer_expected = dec2bin(question_parameter)
		dec_list = generate_cand_list(question_parameter, interval=4, amount=5, limit=True, lim_min = 0, lim_max=2*question_parameter)
		bin_list = list_dec2bin(dec_list)
		cand_list = random_order(bin_list)
		session['cand_list'] = cand_list
	else:
		question_id = 1
		question_parameter = 100
		answer_expected = dec2bin(question_parameter)
		cand_list = session['cand_list']
	'''
	# check if answer is correct
	if request.method == 'POST':
		print "answer got {0}".format(request.form['candidate'])
		if request.form['candidate'] == answer_expected:
			print "correct answer"
			session['cand_list'] = cand_list
			return redirect(url_for('report_result', \
				question_id=question_id, \
				question_parameter = question_parameter, \
				selected=request.form['candidate']))
		else:
			print ["wrong answer", request.form['candidate'], "supposed to be {0}={1}".format(question_parameter, answer_expected)]
	return render_template('single_question_layout.html', \
		question_id = question_id, \
		question_parameter = question_parameter, \
		cand_list=cand_list)

@app.route('/result', methods=['GET', 'POST'])
def report_result():
	question_id = request.args['question_id'] #session['messages']
	cand_list = session['cand_list']
	selected = request.args['selected']
	question_parameter = request.args['question_parameter']
	print "candidate list {0}, length {1}".format(session['cand_list'], len(session['cand_list']))
	return render_template('single_result_layout.html', \
		question_id = question_id, \
		question_parameter = question_parameter, \
		selected = selected, \
		cand_list = cand_list )



if __name__ == '__main__':
	app.run()