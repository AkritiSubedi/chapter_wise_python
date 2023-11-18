# Write a program to greet all the person names storedd in a list l1 and which starts with s

l1 = ["AKriti", "Shyam", "Hari", "Sita", "Sitaram", "Riti"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)