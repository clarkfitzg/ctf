import column_text_format as ctf
# Local
# reader = ctf.reader('vgsales')
# col = reader["EU_Sales"]
# z = iter(col)
# print(next(z))

# a = iter(reader)
# print(next(a))
# S3
reader = ctf.reader('vgsales', bucket_name = 'julian-test-1')
col = reader["EU_Sales"]
print(reader.columns)
z = iter(col)
print(next(z))

a = iter(reader)
print(next(a))