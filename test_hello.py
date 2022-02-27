import hello

class TestHello():
    def test_add(self):
        h = hello.Hello()
        if h.add(2, 3) != 5:
            print('FAILED')
            exit(1)
        print('PASSED')

        if h.add(2, 5) != 7:
            print('FAILED')
            exit(1)
        print('PASSED')

if __name__ == '__main__':
    t = TestHello()
    t.test_add()