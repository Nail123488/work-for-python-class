a = input("The Slug")
b = a.lower()
c = b.spilt()
d = []
for word in c:
    if word != ("a", "the"):
        d.append(word)
slug="-". join(d)
slug=slug[:25]
print(f"Slug={slug}")