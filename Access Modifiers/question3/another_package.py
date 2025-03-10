from public_example import PublicExample

class DifferentPackageClass:
    def access_public(self):
        obj = PublicExample()
        print("Accessing Public Field from Different Package")
        print("Name:", obj.name)
        obj.public_method()

# Different Package Object
obj = DifferentPackageClass()
obj.access_public()
