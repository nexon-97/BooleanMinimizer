from table_import import CsvTableLoader
from expression_generator import TableOfTruthExpressionGenerator
from optimizer import BooleanExpressionOptimizer
from printer import StandardExpressionPrinter
	

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
