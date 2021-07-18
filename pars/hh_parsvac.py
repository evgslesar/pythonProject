from headhunter import get_jobs as hh_get_jobs
from so import get_jobs as so_get_jobs
import csv

'''
With hh.ru it works in repl.it doesn't work on local PC
'''

def save_to_csv(jobs):
  file = open('test.csv', mode='w')
  writer = csv.writer(file)
  writer.writerow(['title', 'company', 'location', 'link'])
  for job in jobs:
    writer.writerow(list(job.values()))
  return


hh_jobs = hh_get_jobs()
so_jobs = so_get_jobs()

jobs = hh_jobs + so_jobs

save_to_csv(jobs)