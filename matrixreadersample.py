import sys
import numpy as np

mat = []

with open('data.txt', 'r', encoding='utf-8') as fin:
    for line in fin.readlines():
        row = []
        toks = line.split(' ')
        for tok in toks:
            try:
                num = float(tok)
            except ValueError:
                print(e, file=sys.stderr)
                continue
            row.append(num)
        mat.append(row)

m = np.matrix(mat)
print(m)

