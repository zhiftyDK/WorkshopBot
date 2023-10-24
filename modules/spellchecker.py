import re
import random
from nltk.corpus import words
import nltk
nltk.download("words")

async def spellchecker(message):
    invalidwordlist = []
    for word in message.content.split(" "):
        if re.sub(r"[^\w]", "", word.lower()) not in words.words():
            invalidwordlist.append(f"'{word}'")
    if len(invalidwordlist) > 0:
        sentences = [
            "You are so fucking bad at spelling!",
            "You're a freaking disgrace!",
            "Try attending your classes for once!",
            "No way your IQ is higher than 80!",
            "Someone should teach you some spelling!",
            "You parents must not be proud!"
        ]
        await message.channel.send(f"<@{message.author.id}> You spelled {' '.join(sum([[i, 'and'] for i in invalidwordlist], [])[:-1])} wrong! {random.choice(sentences)}")