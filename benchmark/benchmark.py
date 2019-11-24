import sys
import codecs
import time
import math

sys.path.append('../')
from ahocorasick import Dictionary

if len(sys.argv) != 3:
    sys.exit(1)
else:
    dict_path = sys.argv[1]
    text_path = sys.argv[2]

    patterns = []
    with codecs.open(dict_path, 'r', 'utf-8', errors='replace') as f:
        for pattern in f:
            pattern = pattern.strip()
            patterns.append(pattern)

    with codecs.open(text_path, 'r', 'utf-8', errors='replace') as f:
        text = f.read()

    start = time.time()
    d = Dictionary(patterns)
    count = sum((1 for _ in d.matches(text)))
    end = time.time()
    ellapsed = (end - start) * 1000.0
    text_size = len(text)
    dict_size = sum((len(p) for p in patterns))
    print('{},{},{},{},{},{},{},{}'.format(
        dict_path,
        dict_size,
        text_path,
        text_size,
        count,
        ellapsed,
        math.log(ellapsed, 2),
        ellapsed / (text_size + dict_size)
        ))
