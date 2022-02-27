class Hello:
    def say(self):
        print('Hello World!')
    def add(self, x, y):
        return x + y

if __name__ == "__main__":
    h = Hello()
    h.say()
    print(h.add(2, 3))