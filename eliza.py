import re
import random

REFLECTIONS = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "i'm": "you are",
    "my": "your",
    "are": "am",
    "you've": "i have",
    "you'll": "i will",
    "your": "my",
    "yours": "mine",
    "you": "i",
    "me": "you",
    "myself": "yourself",
    "yourself": "myself",
}


def reflect(fragment):
    words = fragment.strip().split()
    result = []
    for word in words:
        stripped = word.strip(".,!?;:").lower()
        result.append(REFLECTIONS.get(stripped, stripped))
    return " ".join(result)


RULES = [
    (r"\bi'?m (depressed|sad)\b",
     ["I am sorry to hear you are {0}"]),

    (r"\bi am (depressed|sad)\b",
     ["Why do you think you are {0}"]),

    (r"\bi need (.+)",
     ["What would it mean to you if you got {0}?"]),

    (r"\ball\b",
     ["In what way?"]),

    (r"\balways\b",
     ["Can you think of a specific example?"]),

    (r"\bmy\s+(.+)",
     ["Your {0}"]),

    (r"\bi\s+(.+)",
     ["Do you really think so?",
      "Why do you say that you {0}?",
      "Do you doubt that you {0}?"]),

    (r".*\?$",
     ["Why do you ask that?",
      "Please consider whether you can answer your own question.",
      "Why don't you tell me?"]),
]

DEFAULT_RESPONSES = [
    "Please tell me more.",
    "Can you elaborate on that?",
    "Why do you say that?",
    "I see.",
    "How does that make you feel?",
    "Let's explore that a bit further.",
]

QUIT_WORDS = {"bye", "quit", "exit"}


def strip_trailing_punctuation(text):
    return text.strip().rstrip(".!?")


def eliza_response(user_input):
    text = strip_trailing_punctuation(user_input)

    for pattern, responses in RULES:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            groups = match.groups()
            if groups:
                filled = [reflect(g) for g in groups]
                response = random.choice(responses).format(*filled)
            else:
                response = random.choice(responses)
            return response.upper()

    return random.choice(DEFAULT_RESPONSES).upper()


def main():
    print("Hello, I am ELIZA. How are you feeling today?".upper())

    while True:
        try:
            user_input = input("> ")
        except EOFError:
            break

        if not user_input.strip():
            continue

        if user_input.strip().lower() in QUIT_WORDS:
            print("Goodbye. Take care of yourself.".upper())
            break

        print(eliza_response(user_input))


if __name__ == "__main__":
    main()
