import csv


def trim_list(a):
	return list(map(lambda x: x.strip(), a))
	

class TableLoader:
	def load(path):
		raise NotImplementedError()

	
class CsvTableLoader(TableLoader):
	def load(self, path):
		table = {}

		with open(path, 'r') as f:
			reader = csv.reader(f)
		
			types = reader.__next__()
			header = reader.__next__()
		
			table['header'] = list(zip(trim_list(header), trim_list(types)))
			table['items'] = []
		
			for row in reader:
				if len(row) == len(header):
					table['items'].append(list(map(lambda x: int(x), row)))
		
		return table
	