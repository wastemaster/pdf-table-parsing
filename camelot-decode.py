import camelot

# PDF file to extract tables from
file = "tata-steel-hi-lite-electrical-steel-no35-1750h-datasheet-en.pdf"


# extract all the tables in the PDF file
tables = camelot.read_pdf(file, pages='all')

# number of tables extracted
print("Total tables extracted:", tables.n)

# print the first table as Pandas DataFrame
print(tables[0].df)
print(tables[1].df)
print(tables[2].df)
print(tables[3].df)
