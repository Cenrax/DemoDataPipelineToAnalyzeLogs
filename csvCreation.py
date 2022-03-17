def build_csv(lines, file, header=None):
    if header:
        lines = [header] + [l for l in lines]
    writer = csv.writer(file, delimiter=',')
    writer.writerows(lines)
    file.seek(0)
    return file

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
    
contents = csv_file.readlines()
