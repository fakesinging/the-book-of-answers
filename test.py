import json
import random

# 50 vague and mysterious answers
answers = [
    "It is certain, though not in the way you expect.",
    "A better question will lead to a better answer.",
    "The answer lies in silence.",
    "You already know.",
    "Not now, but soon.",
    "Yes… if you're willing to pay the price.",
    "Only if the stars align.",
    "Rethink everything.",
    "Trust the unknown.",
    "It’s not yours to decide.",
    "Step away and return later.",
    "Yes, but not for long.",
    "You’re asking the wrong question.",
    "Let it go.",
    "The timing is off.",
    "An opportunity will present itself.",
    "Yes, but with a twist.",
    "The answer is hidden in plain sight.",
    "You'll regret it if you don’t.",
    "The winds are shifting in your favor.",
    "Definitely not. Or maybe.",
    "The outcome depends on your patience.",
    "There is more than one answer.",
    "Listen to your intuition.",
    "Prepare for the unexpected.",
    "No, but it will make sense later.",
    "What you seek is also seeking you.",
    "Consider the consequences.",
    "The universe has other plans.",
    "Let time reveal the truth.",
    "It will come when you least expect it.",
    "A detour will take you there.",
    "The signs are unclear.",
    "Now is the perfect time.",
    "You must decide on your own.",
    "Yes, but tread carefully.",
    "You won't like the answer.",
    "Try again with a clear mind.",
    "Someone else holds the key.",
    "What would your future self say?",
    "This isn’t the end — it’s the beginning.",
    "Caution is your ally.",
    "You're looking in the wrong place.",
    "The answer is changing.",
    "This question has no answer… yet.",
    "You will soon understand why.",
    "Let curiosity guide you.",
    "Ask with a sincere heart.",
    "It depends on your next move.",
    "The truth is not ready to be known."
]

random_answers = []
for i in range(1):
    answer = answers[random.randint(0, 10)]
    if(answer in random_answers):
        continue
    print(answer)
    random_answers.append(answer)

my_list = ["Python", "C++", "Java"]
data = {f"{i}": value for i, value in enumerate(my_list)}

json_string = json.dumps(data, indent = 4)
print(json_string)


# print(random_answers)