class Memento:
    def __init__(self, state):
        self.state = state

class Originator:
    def __init__(self, state):
        self.state = state

    def save(self):
        return Memento(self.state)

    def restore(self, memento):
        self.state = memento.state

class Caretaker:
    def __init__(self, originator):
        self.stack = []
        self.originator = originator

    def save_state(self):
        self.stack.append(self.originator.save())

    def undo(self):
        if self.stack:
            self.originator.restore(self.stack.pop())

# Client code
originator = Originator("State1")
caretaker = Caretaker(originator)

for state in ["State1", "State2", "State3"]:
    originator.state = state
    caretaker.save_state()

for _ in range(2):
    caretaker.undo()
    print(f"Restored to: {originator.state}")
