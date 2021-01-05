import re 
import sys 
import csv
import operator 

# add to info csv
def generate_report(rows, filename):
     with open(filename, 'w') as file:
          writer = csv.writer(file)
          writer.writerows(rows)

#find type of error
def ERROR(line):
     search = re.search(r'ERROR (.*)\(.*\)', line)
     return search[1]

#add username to csv
def USERNAME(line):
     search = re.search(r'\(([\S]+)\)',line)
     return search[1]

def create_dict(file):
     error, name = {}, {}
     with open(file) as f:
          for line in f:
               i = 0 # i=0 if info, i=1 if error 
               user = USERNAME(line) #get user
               if 'ERROR' in line:
                    #type of error, frequency of error
                    i = 1
                    err_type = ERROR(line)
                    error[err_type] = error.get(err_type, 0) + 1
               name[user] = name.get(user,[0,0])
               name[user][i] += 1

          error_sorted = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
          name_sorted = sorted(name.items(), key = operator.itemgetter(0))
          name_sorted = [ (k, v[0], v[1]) for (k,v) in name_sorted]

     return error_sorted, name_sorted

if __name__ == '__main__':
     file = sys.argv[1]
     error, name = create_dict(file)
     error.insert(0, ['Error', 'Frequency'])
     generate_report(error, 'report_errors.csv')
     name.insert(0, ['Name', 'INFOS', 'ERRORS'])
     generate_report(name, 'report_users.csv')