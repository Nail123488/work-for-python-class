b = input("Enter the title").lower()
c = b.split()
filtered = []
for w in c:
    if w not in ("a","the"):
        filtered.append(w)
slug = "-". join(filtered)
slug = slug[:25]
print(f"Slug = {slug}")