a = {
    u'data': [
        [u'2013-03-19', u'1363762799', u'4004658'],
        [u'2013-03-20', u'1363849199', u'4756668']
    ],
    u'columns': [
        u'dt_pst',
        u'timestamp',
        u'count'
    ]
}

# Find the index of 'timestamp'
timestamp_index = a['columns'].index('timestamp')

# Extract timestamp values and find the max
max_timestamp = max(int(row[timestamp_index]) for row in a['data'])

print(max_timestamp)  # Output: 1363849199
