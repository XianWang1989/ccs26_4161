
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

# Extract the 'timestamp' values and convert them to integers
max_timestamp = max(int(item[1]) for item in a[u'data'])

print(max_timestamp)  # Output: 1363849199
