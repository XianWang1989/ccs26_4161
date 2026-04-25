
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

# Extracting the timestamp values
timestamps = [int(item[1]) for item in a[u'data']]

# Getting the maximum timestamp value
max_timestamp = max(timestamps)

print(max_timestamp)  # Output: 1363849199
