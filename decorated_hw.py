from main import create_dec_logger

class FlatIterator:
	def __init__(self, item_list):
		self.start = 0
		self.item_list = item_list
		self.unpacked_list_item = list()
		self.unpack_list_items()
		self.end = len(self.unpacked_list_item) - 1

	def __iter__(self):
		self.cursor = self.start - 1
		return self

	def __next__(self):
		self.cursor += 1
		if self.cursor > self.end:
			raise StopIteration
		return self.unpacked_list_item[self.cursor]

	def unpack_list_items(self):

		def is_iterable(current_item):
			try:
				_ = iter(current_item)
			except TypeError:
				return False
			return True

		def unpack(current_list):
			for el in current_list:
				if type(el) != str and is_iterable(el):
					unpack(el)
				else:
					self.unpacked_list_item.append(el)

		unpack(self.item_list)


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

for item in FlatIterator(nested_list):
	print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

# ---------------
# 2nd task


def flat_generator(cur_list):

	def is_iterable(current_item):
		try:
			_ = iter(current_item)
		except TypeError:
			return False
		return True

	@create_dec_logger('decorated_hw.txt')
	def unpack(current_list, curr_res):
		for el in current_list:
			if type(el) != str and is_iterable(el):
				unpack(el, curr_res)
			else:
				curr_res.append(el)
	res = list()
	unpack(cur_list, res)
	for curr_item in res:
		yield curr_item


gen1 = flat_generator(nested_list)
print(gen1)
for item in gen1:
	print(item)