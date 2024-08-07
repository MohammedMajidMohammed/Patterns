class Adaptee:
    def specific_request(self):
        return "Adaptee's specific request"

class Target:
    def request(self):
        return "Target's generic request"

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: {self.adaptee.specific_request()}"

# Client code
adaptee = Adaptee()
adapter = Adapter(adaptee)

print(adapter.request())
