import random
import copy

def dec2bin(dec_num):
	return bin(dec_num)[2:]

def pick_randint(lim_min, lim_max):
	return random.randint(lim_min, lim_max)

def list_dec2bin(dec_list):
	bin_list = []
	for dec_num in dec_list:
		bin_list.append(dec2bin(dec_num))
	return bin_list

def list_mapfunc(func, para_list):
	result_list = []
	for para in para_list:
		result_list.append(func(para))
	return result_list

def generate_para_list(seed, interval=2, amount=4, limit=False, lim_min = 0, lim_max = -1):
	candidate_list = [seed]
	for i in range(amount - 1):
		tmp_len = len(candidate_list)
		tmp_min = candidate_list[0]
		tmp_max = candidate_list[tmp_len - 1]
		if limit:
			if tmp_min - interval < lim_min:
				direction = 1
				if tmp_max + interval > lim_max:
					assert False, "ERROR: limitation of the value range too tight"
			elif tmp_max + interval > lim_max:
				direction = 0
			else:
				direction = pick_randint(0, 1)
		else:
			direction = pick_randint(0, 1)
		if direction == 0: # front
			candidate_list.insert(0, tmp_min - interval)
		else: # end
			candidate_list.append(tmp_max + interval)
	return candidate_list

def random_order(elem_list):
	copy_list = copy.deepcopy(elem_list)
	random.shuffle(copy_list)
	return copy_list

def generate_cand_list(func, question_parameter, interval=4, amount=5, limit=False, lim_min = -1, lim_max=0):
	answer_expected = func(question_parameter)
	dec_list = generate_para_list(question_parameter, interval=interval, amount=amount, limit=limit, lim_min = lim_min, lim_max=lim_max)
	bin_list = list_mapfunc(func, dec_list)
	cand_list = random_order(bin_list)
	return answer_expected, cand_list