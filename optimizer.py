

class BooleanExpressionOptimizer():
	def optimize(self, expressions):
		optimized = []
		
		for expression in expressions:
			expression_copy = expression[:] # Copy expression
			
			while self.optimization_iteration(expression_copy[1]):
				pass
				
			optimized.append(expression_copy)
				
		return optimized
				
	def join_pairs(self, expression, i, j, optimized_idx):
		joined = []
		for k in range(len(expression[i])):
			if k != optimized_idx:
				joined.append(expression[i][k])
	
		expression[i] = joined
		del expression[j]
				
	def find_optimization(self, expression, i, j):
		# Check components length equality
		length = len(expression[i])
		if length != len(expression[j]):
			return -1
			
		diff_idx = -1
		diff_found = False
		
		for k in range(length):
			if expression[i][k] != expression[j][k]:
				if diff_found:
					return -1
				else:
					diff_found = True
					diff_idx = k
					
		return diff_idx
				
	def optimization_iteration(self, expression):
		for i in range(len(expression) - 1):
			for j in range(i + 1, len(expression)):
				optimized_idx = self.find_optimization(expression, i, j)
				
				if optimized_idx != -1:
					self.join_pairs(expression, i, j, optimized_idx)
					return True
	
		return False
		