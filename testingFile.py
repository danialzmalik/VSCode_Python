# from collections import defaultdict

# d = defaultdict(list)

# d["c"].append("last")
# d["a"].append((1,"first"))
# d["b"].append(2)
# d["a"].append((3,"third"))

# d = sorted(d.keys())

# print(d)
# for key in d.keys():
#     print(key)
#     for value in d.get(key):
#         print(f"\t{value}")

lst = [
 ('a', [1, 2, 3]),
 ('b', ['blah', 'bhasdf', 'asdf']),
 ('c', ['one', 'two']),
 ('d', ['asdf', 'wer', 'asdf', 'zxcv'])
]
print(lst)
d = dict(lst)
print(d)