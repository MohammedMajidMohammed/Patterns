class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received: {message}")

# Example usage
subject = Subject()

observers = [Observer() for _ in range(2)]
for observer in observers:
    subject.attach(observer)

subject.notify("Hello!")

subject.detach(observers[1])

subject.notify("Goodbye!")
