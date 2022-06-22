import random
from time import sleep

kursanci = []

class Losowanko:
    def __init__(self, kursanci):
        self.kursanci = kursanci

    def losuj(self):
        share_screen = random.choice(self.kursanci)
        self.kursanci.remove(share_screen)
        print(f"Ekran udostępni.....")
        for second in range(5, -1, -1):
            print(f"{second}...")
            sleep(1)
        print(share_screen)


losowanko = Losowanko(kursanci)
while losowanko.kursanci:
    input("losować? >enter<")
    losowanko.losuj()

print("reload the program")