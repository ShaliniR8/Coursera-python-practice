import csv
from collections import defaultdict


def create_dictionary(filename):
     d = defaultdict(int)
     csv.register_dialect( 'emp-dialect', skipinitialspace=True)
     with open(filename) as emp:
          emp_reader = csv.DictReader(emp, dialect = 'emp-dialect')
          for row in emp_reader:
               d[row['Department']] = d.get(row['Department'], 0) + 1
     return d


def generate_report(dictionary):
     sorted_dep = sorted(dictionary, key=dictionary.get, reverse=True)
     with open('report.txt', mode='w') as report_writer:
          for dep in sorted_dep:
               report_writer.write(f'{dep} : {dictionary[dep]}\n')


filename = 'employees.csv'
dic = create_dictionary(filename)
generate_report(dic)