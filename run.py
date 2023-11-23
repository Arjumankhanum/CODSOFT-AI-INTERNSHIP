import random

def ask_random_question():
    questions = [
        "What's your favorite Quote?",
        "What's the last thing you did and enjoyed?",
        "If you had a superpower for a day, what would it be?",
        "What's your go-to comfort place?",
        "If you could invent a new gadget what would it be?",
        "What's the most interesting fact you know",
        "What's your favorite game and why?",
        "If you could time travel, would you go to the past or the future?"
    ]

    random_question = random.choice(questions)
    return random_question

def get_user_response():
    return input("Your answer: ")

def main():
    print("Welcome to the ChatBot! Let's have an interesting conversation.")
    while True:
        question = ask_random_question()
        print(question)

        user_answer = get_user_response()
        response = respond_to_answer(user_answer)
        print(response)

        continue_chat = input("Do you want to continue the conversation? (yes/no): ")
        if continue_chat.lower() != "yes":
            print("Goodbye! Have a great day!")
            break

def respond_to_answer(answer):
    if "favorite" in answer.lower():
        return f"Ah, {answer}! That says a lot about you."
    elif "superpower" in answer.lower():
        return f"A {answer} would be incredible! What would you do with that power?"
    elif "visit" in answer.lower():
        return f"{answer} sounds like an amazing place! What attracts you to it?"
    elif "skill" in answer.lower():
        return f"Learning {answer} is a fantastic choice! What sparked your interest?"
    else:
        return f"Interesting choice. Tell me more about {answer}."



if __name__ == "__main__":
    main()