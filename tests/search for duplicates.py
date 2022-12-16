a = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]

b = []
for i in range(0, len(a)):
    if a[i] not in a[i+1:]:
        b.append(a[i])

print(b)
