import csv

log = open('example_log.txt')
parsed = parse_log(log)
file = open('temporary.csv', 'r+')
csv_file = build_csv(
    parsed,
    file,
    header=[
        'ip', 'time_local', 'request_type',
        'request_path', 'status', 'bytes_sent',
        'http_referrer', 'http_user_agent'
    ]
)
import csv
import itertools

def count_unique_request(csv_file):
    reader = csv.reader(csv_file)
    header = next(reader)
    idx = header.index('request_type')
    
    uniques = {}
    for line in reader:
        if not uniques.get(line[idx]):
            uniques[line[idx]] = 0
        uniques[line[idx]] += 1
    return uniques

log = open('example_log.txt')
parsed = parse_log(log)
file = open('temporary.csv', 'r+')
csv_file = build_csv(
    parsed,
    file,
    header=[
        'ip', 'time_local', 'request_type',
        'request_path', 'status', 'bytes_sent',
        'http_referrer', 'http_user_agent'
    ]
)
uniques = count_unique_request(csv_file)
print(uniques)
