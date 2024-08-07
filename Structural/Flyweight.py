class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, shared):
        if shared not in self.flyweights:
            self.flyweights[shared] = shared
        return self.flyweights[shared]

# Client code
factory = FlyweightFactory()

fw1 = factory.get_flyweight("Shared1")
print(f"Shared: {fw1}, Unique: UniqueA")

fw2 = factory.get_flyweight("Shared1")
print(f"Shared: {fw2}, Unique: UniqueB")

fw3 = factory.get_flyweight("Shared2")
print(f"Shared: {fw3}, Unique: UniqueC")
