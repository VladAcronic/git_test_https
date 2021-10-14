
################################################################################
# in this file main architecture of data processing is placed

class Fibo ():
	"""
		class contain fibo number calculation functions
	"""
	def __init__(self, fibo_count):
			self.row = [1, 1]
			self.fibo_count = fibo_count
			self.fibo_number = None
	
	def __calculate_last_fibo_number (self):
		'''
			function calculate indexed fibo number 
		'''
		fibo_index = len (self.row) + 1		
		indexed_fibo_number = self.row[-1] + self.row[-2]
		last_fibo_data = (fibo_index, indexed_fibo_number)
		#print (f"last_fibo_data: {last_fibo_data}")
		return last_fibo_data
	
	def calculate_fibo_number (self):
		'''
			before given fibo_count		
		'''
		# !--todo--! make check that fibo_count more than 2 and less then some unreal 
			#for calculation number
	
		for fibo_data in self.row:
			last_fibo_data = self.__calculate_last_fibo_number()
			
			if last_fibo_data[0] < self.fibo_count:
				self.row.append (last_fibo_data[1])
			else: 
				self.row.append (last_fibo_data[1])
				self.fibo_number = last_fibo_data[1]
				return self.fibo_number
	
	def __repr__(self):
		#!--todo--! implement check for print numeric parametrs, not NoneType
		return f"\nfibo number with index {self.fibo_count} is {self.fibo_number}"
