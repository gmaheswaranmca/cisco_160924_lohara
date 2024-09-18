class Bird:
    def fly(self):
        return 'bird is flying...'
class Crow(Bird):
    def fly(self):
        return 'crow is flying...'
class Parrot(Bird):
    def fly(self):
        return 'parrot is flying...'
class Eagle(Bird):
    pass 

def test_fly(bird):
    print(bird.fly())

crow1 = Crow()
parrot1 = Parrot()
parrot2 = Parrot()
eagle1 = Eagle()
test_fly(crow1)
test_fly(parrot1)
test_fly(parrot2)
test_fly(eagle1)