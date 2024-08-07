class Light:
    def turn_on(self):
        return "Light is on"

    def turn_off(self):
        return "Light is off"

class Command:
    def __init__(self, light, action):
        self.light = light
        self.action = action

    def execute(self):
        return getattr(self.light, self.action)()

# Example usage
light = Light()
light_on_command = Command(light, "turn_on")
light_off_command = Command(light, "turn_off")

print(light_on_command.execute())
print(light_off_command.execute())
