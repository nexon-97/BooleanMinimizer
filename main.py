from table_import import CsvTableLoader
from expression_generator import TableOfTruthExpressionGenerator
from optimizer import BooleanExpressionOptimizer
from printer import StandardExpressionPrinter
	
	
def format_expression(components):
	formatted_components = []
	for item in components:
		a = list(map(lambda x: x[0] if x[1] else '!' + x[0], item))
		formatted_components.append('(%s)' % (' & '.join(a)))

	return ' | '.join(formatted_components)
	
# =========================================================================

if __name__ == "__main__":
	from sys import argv
	
	if len(argv) > 1:
		table_path = argv[1]

		loader = CsvTableLoader()
		table = loader.load(table_path)
		
		expression_generator = TableOfTruthExpressionGenerator()
		expressions = expression_generator.generate(table)
		
		optimizer = BooleanExpressionOptimizer()
		optimized = optimizer.optimize(expressions)
		
		printer = StandardExpressionPrinter()
		for expression in optimized:
			print(printer.print_expression(expression))
	else:
		print('Pass table of truth path in order to generate expressions!')
