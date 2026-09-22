a = input()
b = a.lower()
c = b.split()
filtered = []
for word in c:
    if word not in  ("a", "the"):
        filtered.append(word)
slug = "-". join(filtered)
slug = slug[:25]
print(f"Slug={slug}")