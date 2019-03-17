class Chubs:
    fat = 0 #pounds
    name = 'generic chubs'
    def eat(self, pounds_of_food):
        self.fat = self.fat + pounds_of_food / 2
        print("burp")
        poop = pounds_of_food / 2
        return poop
    def __init__(self, pounds, name):
        print('hit init')
        self.fat = pounds
        if(name != ''):
            self.name = name

def main():
    alan = Chubs(300, 'Alan')
    print(alan.fat)
    print(alan.name)
    alans_poop = alan.eat(50)
    print(alan.fat)
    print(alans_poop)
    baron = Chubs(100, 'Baron')
    print(baron.fat)
    print(baron.name)
    barons_poop = baron.eat(alans_poop)
    print(baron.fat)

    alan.eat(barons_poop)
    print(alan.fat)

    eric = Chubs(50, '')
    print(eric.fat)
    print(eric.name)
main()