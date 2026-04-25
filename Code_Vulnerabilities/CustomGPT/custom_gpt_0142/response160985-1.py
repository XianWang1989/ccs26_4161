
# Your dictionary
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

# Extract the index for the 'timestamp' column
timestamp_index = a[u'columns'].index(u'timestamp')

# Use a generator expression to find the max value for 'timestamp'
max_timestamp = max(row[timestamp_index] for row in a[u'data'])

# Print the result
print(max_timestamp)  # Output: 1363849199
