import random
import time

class Setup:
    def __init__(self):
        print("WELCOME TO HARD TYPING TRAINING")
        self.words = list()
        self.practice_time = 0
        self.used_index = list()
        self.count = 0
        with open('words.txt') as file:
            for line in file:
                if len(line) != 1 or len(line) < 10:
                    self.count += 1
                    self.words.append(line.replace("\n",""))
    
    def get_time(self):
        self.practice_time = input("How long do you have to Practice (mins)?\n")
        try:
            self.practice_time = 60*int(self.practice_time)
            print("Practice time set to: {} seconds".format(self.practice_time))
        except ValueError:
            print("Enter a valid number in minutes")
            self.get_time()

    def generate_rand_words(self):
        rand_words = list()
        while len(rand_words) < 8:
            index = random.randint(0, self.count)
            if index not in self.used_index:
                self.used_index.append(index)
                rand_words.append(self.words[index])
        return rand_words

    def grade_words(self, words_list, user_string):
        if isinstance(user_string, str):
            total_words = len(words_list)
            user_in_list = user_string.split()
            user_in_list = user_in_list[:total_words]
            corrects = 0
            for i in range(len(user_in_list)):
                if words_list[i] == user_in_list[i]:
                    corrects +=1
            return corrects
        else:
            print("Invalid input by user")
            return 0

    def load_application(self):
        if not self.practice_time:
            self.get_time()
        start_ts = time.time()
        corrects = 0
        total_words = 0
        while time.time() - start_ts < self.practice_time:
            words_list = master.generate_rand_words()
            print(" ".join(words_list))
            user_in = input()
            corrects += master.grade_words(words_list, user_in)
            total_words += len(words_list)
        print("Your Accuracy is {:.2f} ".format(corrects*100/total_words))
        retry = input("Do you want to start again?(y/n)")
        if retry == "y":
            self.load_application()
        else:
            print("Bye, see you again !")

master = Setup()
master.load_application()