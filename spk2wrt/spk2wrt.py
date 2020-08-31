
class conversionSystem(object):
	"""docstring for ClassName"""
	def __init__(self, text):
		self.text = text.lower()
		self.numbers = {
			'type1':{
				'one':'1',
				'two':'2',
				'three':'3',
				'four':'4',
				'five':'5',
				'six':'6',
				'seven':'7',
				'eight':'8',
				'nine':'9',
				'zero':'0',
			},

			'type2':{
				'ten':'10',
				'eleven':'11',
				'twelve':'12',
				'thirteen':'13',
				'fourteen':'14',
				'fifteen':'15',
				'sixteen':'16',
				'seventeen':'17',
				'eighteen':'18',
				'nineteen':'19',
			},

			'type3':{
				'twenty':'20',
				'thirty':'30',
				'forty':'40',
				'fifty':'50',
				'sixty':'60',
				'seventy':'70',
				'eighty':'80',
				'ninety':'90',
			},

			'type4':{
				'hundred':'100',
				'thousand':'1000',
				'million':'1000000',
				'billion':'1000000000',
			}

		}


	def for_hundred(self, nums):
		val = 0
		for v in nums:
			try:
				val = val + int(self.numbers['type1'][v])
			except:
				try:
					val = val + int(self.numbers['type2'][v])
				except:
					val = val + int(self.numbers['type3'][v])
		if val!=0:
			return val
		else:
			return 1


	def get_value(self, nums):
		val = 0
		K=0
		if 'hundred' in nums:
			k = nums.index('hundred')
			n_temp = nums[:k]
			n_t = self.for_hundred(n_temp)
			val = val + (n_t*100)
			K = k+1
		for v in range(K,len(nums)):
			try:
				val = val + int(self.numbers['type1'][nums[v]])
			except:
				try:
					val = val + int(self.numbers['type2'][nums[v]])
				except:
					val = val + int(self.numbers['type3'][nums[v]])
		return val


	def word_to_num(self, words):
		num = words
		current_val = []
		check_type4 = dict()
		i1=0
		for i in range(len(num)):
			check = False
			if num[i] in self.numbers['type4']:
				check_type4[num[i],i1] = i
				i1 += 1

		temp_store = []
		for key in check_type4:
			temp_store.append([key[0],check_type4[key]])

		i=1
		while(i<len(temp_store)):
			checking_t=False
			cur_val = int(self.numbers['type4'][temp_store[i][0]])
			pre_val = int(self.numbers['type4'][temp_store[i-1][0]])
			if cur_val > pre_val:
				temp_store.pop(i-1)
				checking_t = True
			if not checking_t:
				i=i+1
		for i in range(len(temp_store)):
			key_val = int(self.numbers['type4'][temp_store[i][0]])
			upto = temp_store[i][1]
			from_ = 0
			if i>0:
				from_ = temp_store[i-1][1]+1
			now = num[from_:upto]
			t_val = self.get_value(now)
			current_val.append(t_val*key_val)
		for key in check_type4:
			checking=True
		if key:
			if check_type4[key]+1<len(num):
				temp_val = self.get_value(num[check_type4[key]+1:])
				current_val.append(temp_val)
			return sum(current_val)
		current_val.append(self.get_value(num))
		return sum(current_val)
	def dict_check(self, word):
		if (word in self.numbers['type1']) or (word in self.numbers['type2']) or (word in self.numbers['type3']) or (word in self.numbers['type4']):
			return True
		else:
			return False
	def checking(self, words, temp):
		ind = temp
		while(temp>0):
			if self.dict_check(words[temp-1]):
				ind = temp
			else:
				return ind
			temp = temp - 1
		return 0

	def convert_to_written(self, conversion_type):
		words = self.text.split(' ')
		if conversion_type =='make_repetitions': #Make Repetitions
			if words[0].lower()=='double':
				return words[1]*2
			elif words[0].lower()=='triple':
				return words[1]*3
			elif 'times' in words:
				temp = words.index('times')
				num = words[:temp]
				value = self.word_to_num(num)
				result = words[temp+1] * value
				return result
		elif conversion_type == 'spoken_to_written_numbers': #Convert English Numbers to Numericals
				num = words
				return int(self.word_to_num(num))
		elif conversion_type == 'spoken_to_written_english': #Convert Spoken English to Written English
			if 'dollars' in words:
				temp = words.index('dollars')
				ind = self.checking(words, temp)
				if ind==0:
					num = words[:temp]
					words_t = words[temp+1:]
					value = self.word_to_num(num)
					combined_word = ' '.join(map(str, words_t))
					return '$' + str(value) + ' ' + combined_word
				elif ind!=0:
					num = words[ind-1:temp]
					words1 = words[:ind-1]
					words2 = words[temp+1:]
					combined_word1 = ' '.join(map(str, words1))					
					value = self.word_to_num(num)
					combined_word2 = ' '.join(map(str, words2))
					return combined_word1 + ' $' + str(value) + ' ' + combined_word2
			if (('hashtag' in words) or ('hastag' in words)):
				try:
					temp = words.index('hashtag')
				except:
					temp = words.index('hastag')
				num = words[temp+1:]
				num1 = words[:temp]
				combined_word = ''.join(map(str, num))
				combined_word1 = ' '.join(map(str, num1))
				return combined_word1 + ' #' + combined_word