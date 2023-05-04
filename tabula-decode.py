import tabula
import os

tables = tabula.read_pdf("tata-steel-hi-lite-electrical-steel-no35-1750h-datasheet-en.pdf", pages="all")

print(tables[1])

