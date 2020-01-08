#!/usr/bin/python3

import random

""" This is a simple program that simulate a coctail monaco game.
Enter a list of players, and the program will get 1 out per time. """

# global person_id

class Person:
    """Simple person class with First and Second name."""
    def __init__(self, uid, first_name, family_name):
        
        self.first_name = first_name
        self.family_name = family_name

    def print(self):
        print(self.first_name, self.family_name)



class Game:
    """docstring for Game"""

    person_id = 0
    bid_id = 0


    def __init__(self, ):

        self.bids = []
        self.persons = []
        self.persons_out = {}

    def add_person(self, first_name, family_name):

        self.person_id += 1
        person = Person(self.person_id, first_name, family_name)
        self.persons.append(person)
        print("Person added : %s %s %s" %(self.person_id, first_name, family_name))

    def get_person(self, first_name=None, family_name=None):
        results1 = []
        results2 = []

        if first_name is not None:
            
            results1 = [x for x in self.persons if x.first_name == first_name]
            

        if family_name is not None:

            results2 = [x for x in self.persons if x.family_name == family_name]

        results = results1 + results2

        if len(results) == 0:
            print("no results found")

            return None

        if len(results) == 1:
            return results[0]
        
        if len(results) > 1:
            print("too many results refine search")
            return None 

    def add_bid(self, ):

        self.bid_id += 1

        person1_name = input("Enter the name of the first person >>" )
        person1_family_name = input("Enter the family name of the first person >>")
        person1 = self.get_person(first_name=person1_name, family_name=person1_family_name)

        person2_name = input("Enter the name of the second person >>")
        person2_family_name = input("Enter the family name of the second person >>")
        person2 = self.get_person(first_name=person2_name, family_name=person2_family_name)

        amount = float(input("What is the amount? >>"))

        bid = Bid(self.bid_id, person1, person2, amount)
        self.bids.append(bid)
        print("Bid added between %s %s and %s %s of %s$" %(person1.first_name, person1.family_name, person2.first_name, person2.family_name, amount))

    def shuffle_persons(self):
        random.shuffle(self.persons)

    def get_one(self, position):
        the_one = self.persons.pop(0)
        self.persons_out[position] = the_one
        the_one.print()

    def play(self):

        for k in range(len(self.persons)):
            value = input("Ready to pick one person? >>")
            self.get_one(k+1)
        # print(self.persons_out)


    def print_persons_out(self):
        count = 0
        for key in self.persons_out:

            print("%3s %s %s" %(key, self.persons_out[key].first_name, self.persons_out[key].family_name))
            if not ((count+1) % 5):
                print(" ")

            count += 1

class Bid:
    """docstring for Bid"""
    def __init__(self, uid, person1, person2, amount):

        self.person1 = person1
        self.person2 = person2
        self.amount = amount

    def add(self, person1, person2, amount):

        self.person1 = person1
        self.person2 = person2
        self.amount = amount

class Editor(Game):
    def __init__(self):
        game = Game()
        game.add_person('Peter', 'Quill')
        game.add_person('Yondu', 'Udonta')
        game.add_person('Gamora')
        game.add_person('Korath')
        game.add_person('Rocket')
        game.add_person('Groot')
        game.add_person('Drax')

        self.menu_map = {
            "bid": game.add_bid(),
            "test": self.test,
            "change": self.change,
            "quit": self.quit,
        }



    def test(self):
        if self.is_permitted("test program"):
            print("Testing program now...")

    def change(self):
        if self.is_permitted("change program"):
            print("Changing program now...")

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print(
                    """
Please enter a command:
\tbid\tAdd bid
\ttest\tTest the program
\tchange\tChange the program
\tquit\tQuit
"""
                )
                answer = input("enter a command: ").lower()
                try:
                    print("ok")
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")




if __name__ == "__main__":


    Editor().menu()  

    game.add_bid()

    game.shuffle_persons()

    game.play()

    game.print_persons_out()


        
