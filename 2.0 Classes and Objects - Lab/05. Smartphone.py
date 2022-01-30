class Smartphone:
    apps = []
    is_on = False

    def __init__(self, memory):
        self.memory = memory

    def power(self):
        if not self.is_on:
            self.is_on = True
        else:
            self.is_on = False

    def install(self, app, app_memory):
        if self.is_on and self.memory >= app_memory:
            self.apps.append(app)
            self.memory -= app_memory
            return f'Installing {app}'
        if not self.is_on and self.memory >= app_memory:
            return f'Turn on your phone to install {app}'

        return f'Not enough memory to install {app}'

    def status(self):
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'


# --------------------------
smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())

'''
Turn on your phone to install Facebook
Installing Facebook
Installing Messenger
Not enough memory to install Instagram
Total apps: 2. Memory left: 20
'''
