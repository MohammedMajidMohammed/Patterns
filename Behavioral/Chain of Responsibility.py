class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if not self._handle(request) and self.successor:
            self.successor.handle(request)

    def _handle(self, request):
        pass  # To be implemented by subclasses

class HandlerA(Handler):
    def _handle(self, request):
        if request == "A":
            print("HandlerA handled the request")
            return True
        return False

class HandlerB(Handler):
    def _handle(self, request):
        if request == "B":
            print("HandlerB handled the request")
            return True
        return False

class HandlerC(Handler):
    def _handle(self, request):
        if request == "C":
            print("HandlerC handled the request")
            return True
        return False

# Client code
h1 = HandlerA()
h2 = HandlerB(h1)
h3 = HandlerC(h2)

for request in ["A", "B", "C", "D"]:
    h3.handle(request)
