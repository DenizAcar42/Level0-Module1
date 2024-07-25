"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""


def ask_riddle(riddle, answer):
    user_answer = input(riddle + " ").strip().lower()
    if user_answer == answer.lower():
        print("Correct!")
    else:
        print(f"Sorry, the correct answer is: {answer}")


def main():
    riddles = [
        {
            "riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            "answer": "echo"},
        {
            "riddle": "I’m not alive, but I grow; I don’t have lungs, but I need air; I don’t have a mouth, but water kills me. What am I?",
            "answer": "fire"},
        {"riddle": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"}
    ]

    print("Welcome to the Riddle Game!")

    for riddle in riddles:
        ask_riddle(riddle["riddle"], riddle["answer"])

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
