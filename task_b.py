a = input()
b = a.lower()
c = b.spilt()
d = []
for word in c:
    if word != ("a", "the"):
        d.append(word)
slug_str="-". join(d)
slug=slug_str[:25]
print(f"Slug={slug}")