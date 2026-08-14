import random

def fortune_cookie():
    fortunes = [
        "You will ace your DSA exam!",
        "Something amazing is coming your way.",
        "Keep grinding, success is closer than you think.",
        "A bug today, a debug tomorrow.",
        "AI will be your best friend in the future."
    ]

    # pick a random fortune
    print("Your fortune: " + random.choice(fortunes))

fortune_cookie()
