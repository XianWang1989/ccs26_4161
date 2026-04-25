
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

# Extract the 'timestamp' values from the 'data' list
timestamps = [int(entry[1]) for entry in a[u'data']]

# Get the maximum value
max_timestamp = max(timestamps)

print(max_timestamp)  # Output: 1363849199
