import psycopg2
import math

conn = psycopg2.connect("dbname=cnssankey user=xiya")
cur = conn.cursor()

# for i in range(10):
  # cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (i,math.sin(i)))

def make_data_point(first_name, last_name, gender, cohort_year):
  return {
    "first_name": first_name,
    "last_name": last_name,
    "gender": gender,
    "cohort_year": cohort_year
  }

proto_data = [
  ["Mary", "Chen", "F", 2001],
  ["Edward", "Tock", "M", 1997],
  ["Seth", "Tan", "M", 2006],
  ["Xiya", "Yang", "M", 2015],
  ["Yolanda", "Yeo", "F", 2013] 
]

data = [make_data_point(*d) for d in proto_data]

for d in data:
  cur.execute("INSERT INTO student_flow_dashboard_person (first_name, last_name, gender, cohort_year) VALUES (%s, %s, %s, %s);", (d["first_name"],d["last_name"],d["gender"],d["cohort_year"]))


conn.commit()
cur.close()
conn.close()
 
