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
    (r"\bhello\b|\bhi\b|\bhey\b",
     ["Hello. How are you feeling today?",
      "Hi there. What would you like to talk about?"]),

    (r"\bcomputers?\b",
     ["Do computers worry you?",
      "Why do you mention computers?",
      "What do you think machines have to do with your problem?"]),

    (r"\bsorry\b",
     ["Please don't apologize.",
      "Apologies are not necessary.",
      "It's alright, just tell me how you feel."]),

    (r"i remember (.+)",
     ["Do you often think of {0}?",
      "What made you think of {0} just now?",
      "Why do you remember {0} at this moment?"]),

    (r"do you remember (.+)",
     ["Why do you ask if I remember {0}?",
      "What about {0} would you like me to remember?",
      "Why do you think I should recall {0}?"]),

    (r"i dream(?:ed|t)? (?:about|of) (.+)",
     ["How does the dream about {0} make you feel?",
      "Have you dreamed about {0} before?",
      "What do you think {0} represents?"]),

    (r"\b(?:mother|father|sister|brother|family|parents?)\b",
     ["Tell me more about your family.",
      "Who else in your family comes to mind?",
      "Does that have anything to do with your family?"]),

    (r"i'?m (depressed|sad|unhappy)",
     ["I am sorry to hear you are {0}.",
      "How long have you been {0}?",
      "Do you think coming here will help you not to be {0}?"]),

    (r"i am (depressed|sad|unhappy)",
     ["Why do you think you are {0}?",
      "I am sorry to hear you are {0}.",
      "How long have you been {0}?"]),

    (r"i feel (.+)",
     ["Do you often feel {0}?",
      "What makes you feel {0}?",
      "How long have you felt {0}?"]),

    (r"i can'?t (.+)",
     ["How do you know you can't {0}?",
      "Perhaps you could {0} if you tried.",
      "What would it take for you to {0}?"]),

    (r"i need (.+)",
     ["What would it mean to you if you got {0}?",
      "Would it really help you to get {0}?",
      "Are you sure you need {0}?"]),

    (r"because (.+)",
     ["Is that the real reason, {0}?",
      "What other reason might there be?",
      "Does that reason satisfy you?"]),

    (r"are you (.+)\??",
     ["Why does it matter whether I am {0}?",
      "Would you prefer if I were not {0}?",
      "Do you sometimes wish you were {0}?"]),

    (r"\bfriend\b",
     ["Tell me more about your friends.",
      "Why do you bring up friends?",
      "Do your friends know how you feel?"]),

    (r"\byes\b",
     ["You seem quite sure.",
      "OK, but can you elaborate a bit?"]),

    (r"\bno\b",
     ["Why not?",
      "You are being a bit negative.",
      "Are you sure?"]),

    (r"\ball\b",
     ["In what way?",
      "Can you think of a specific example?",
      "What makes you say all?"]),

    (r"\balways\b",
     ["Can you think of a specific example?",
      "Really, always?",
      "When exactly?"]),

    (r"my (.+)",
     ["Your {0}?",
      "Why do you say your {0}?",
      "Tell me more about your {0}."]),

    (r"i (.+)",
     ["Do you really think so?",
      "Why do you say that you {0}?",
      "Do you doubt that you {0}?"]),

    (r"(what|how|why) (.+)\??",
     ["Why do you ask that?",
      "What do you think?",
      "What answer would please you the most?"]),

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
    "Very interesting. Go on.",
    "I'm listening, please continue.",
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
            return response

    return random.choice(DEFAULT_RESPONSES)


def main():
    print("Hello, I am ELIZA. How are you feeling today?")

    while True:
        try:
            user_input = input("> ")
        except EOFError:
            break

        if not user_input.strip():
            continue

        if user_input.strip().lower() in QUIT_WORDS:
            print("Goodbye. Take care of yourself.")
            break

        print(eliza_response(user_input))


if __name__ == "__main__":
    main()
