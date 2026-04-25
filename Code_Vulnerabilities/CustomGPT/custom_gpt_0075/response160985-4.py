
# Example Code Snippet
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

# Extracting maximum timestamp
max_timestamp = max(row[1] for row in a['data']) # row[1] corresponds to 'timestamp'
print(max_timestamp)  # Output: 1363849199
