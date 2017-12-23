class BooleanExpressionPrinter():
	def print_expression(self, expression):
		raise NotImplementedError()
		
		
class StandardExpressionPrinter(BooleanExpressionPrinter):
	def print_expression(self, expression):
		conjunction_parts = []
		
		for conjunction_part in expression[1]:
			printed_conjunction = ' & '.join(list(map(lambda x: x[0] if x[1] else '!' + x[0], conjunction_part)))
			conjunction_parts.append('(%s)' % printed_conjunction)
			
		return '%s = %s' % (expression[0], ' | '.join(conjunction_parts))
		