# Memory Game

A simple command-line memory game written in Python. Test and improve your memory by remembering and recalling a sequence of words displayed by the computer.

## How to Play

1. The computer will display three random words for you to memorize.
2. After the words are displayed, you will have 30 seconds to enter your guess for the sequence of words.
3. Enter your guess by typing the words in the same sequence, separated by spaces.
4. If your guess matches the original sequence, you win! Otherwise, better luck next time.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository:


git clone https://github.com/harshini91/Memorygame_python
cd memory-game


2. Run the game:

```bash
python memory_game.py
```

## Example


Welcome to the Memory Game!
The computer will display three words for you to memorize.

Memorize the following words:
apple banana orange

(You have 30 seconds to input your guess)


Enter the words in the same sequence (space-separated): apple banana orange
Congratulations! You remembered the words correctly. You won!


## Customization

Feel free to customize the `word_list` in the `get_random_words` function to include your own set of words.

```python
def get_random_words():
    word_list = [
        "word1", "word2", "word3",  # Add your own words here
    ]
    return random.sample(word_list, 3)
```

## Acknowledgments

This project is a simple demonstration and can be enhanced further with additional features and improvements. Have fun playing and exercising your memory!
