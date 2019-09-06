from duckduckpy import query
response = query('украина https://t.me/', container='dict')
print(response['related_topics'])
