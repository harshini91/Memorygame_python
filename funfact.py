import random
import time
import threading

def display_words(words):
    print("\nMemorize the following words:")
    for word in words:
        print(word, end=" ", flush=True)
        time.sleep(1)  
        print("\b" * len(word), end=" ", flush=True)  
        time.sleep(1)  

def get_random_words():
    word_list = [
        "apple", "banana", "orange", "grape", "kiwi",
        "python", "java", "csharp", "html", "css",
        "moon", "sun", "star", "planet", "galaxy",
        "cat", "dog", "bird", "fish", "turtle",
        "shashitha" , "chetu" , "harshini" , "bts"
    ]
    return random.sample(word_list, 3)

def user_input_thread(user_input):
    user_input.append(input("\nEnter the words in the same sequence (space-separated): ").split())

def start_memory_game():
    print("Welcome to the Memory Game!")
    print("The computer will display three words for you to memorize.")

    words_to_remember = get_random_words()
    display_words(words_to_remember)

    user_input = []
    input_thread = threading.Thread(target=user_input_thread, args=(user_input,))
    input_thread.start()

    input_thread.join(timeout=30)  

    if input_thread.is_alive():
        print("\nTime's up! You didn't enter your guess in time.")
    else:
        user_guess = user_input[0]
        if user_guess == words_to_remember:
            print("\nCongratulations! You remembered the words correctly. You won!")
        else:
            print("\nSorry, you didn't guess correctly. Better luck next time. You lost.")

if __name__ == "__main__":
    start_memory_game()
