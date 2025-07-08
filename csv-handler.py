#!/usr/bin/python3

import csv
from tabulate import tabulate

class CSVParser:

	def __init__(self, filepath:str) -> None:
		self.csv = [line for line in csv.reader(open(filepath, "r"))]
		self.write(self.csv[0:1][0], self.csv[1:])

	def write(self, headers:list, rows:list) -> None:
		self.headers = headers
		self.rows = rows

	def filter(self, where:str) -> None:
		syntax = ">" if ">" in where else "<" if "<" in where else "="
		args = where.split(syntax)
		self.rows = [row for row in self.filter_syntax(self.headers.index(args[0]), "==" if syntax == "=" else syntax, args[1])]

	def filter_syntax(self, index:int, syntax:str, arg:str) -> list:
		arg_type = "str" if syntax == "==" else "float"
		for row in self.rows:
			if eval(arg_type+"(row[index])"+syntax+arg_type+"(arg)"):
				yield row

	def aggregation(self, aggregate:str) -> None:
		args = aggregate.split("=")
		index = self.headers.index(args[0])
		values = [float(row[index]) for row in self.rows]
		value = 0
		if args[1] == "avg":
			value = round(sum(values)/len(values), 2)
		elif args[1] == "min":
			value = min(values)
		elif args[1] == "max":
			value = max(values)
		self.write([args[1]],[[value]])

	def __str__(self) -> str:
		return tabulate(self.rows, self.headers, tablefmt="psql")

def main():
	import argparse
	parser = argparse.ArgumentParser(description="CSV file handler")
	parser.add_argument("--file", help="Path to the CSV file")
	parser.add_argument("--where", help="Filter ('header=value', 'header<value', 'header>value')")
	parser.add_argument("--aggregate", help="Aggregations ('header=avg', 'header=min', 'header=max')")

	args = parser.parse_args()
	file, where, aggregate = args.file, args.where, args.aggregate
	if not file:
		raise NameError("csv file not specified")

	csv_parser = CSVParser(file)
	if where:
		csv_parser.filter(where)
	if aggregate:
		csv_parser.aggregation(aggregate)
	print(csv_parser)

if __name__ == '__main__':
	main()
