class TableOfTruthExpressionGenerator:
	def generate_conjunction_part(self, table_of_truth, row):
		components = []
			
		for column_idx in range(len(table_of_truth['header'])):
			column = table_of_truth['header'][column_idx]
			
			if column[1] == 'I':
				components.append((column[0], row[column_idx] == 1))
					
		return components
		
		
	def generate_expression(self, table_of_truth, output_idx):
		expression = []
			
		for row in table_of_truth['items']:
			if row[output_idx] == 1:
				expression.append(self.generate_conjunction_part(table_of_truth, row))
				
		return expression
		

	def generate(self, table_of_truth):
		expressions = []
	
		for column_idx in range(len(table_of_truth['header'])):
			column = table_of_truth['header'][column_idx]
			if column[1] == 'O':
				expression = self.generate_expression(table_of_truth, column_idx)
				expressions.append((column[0], expression))
					
		return expressions
		