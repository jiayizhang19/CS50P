import re

def main():
    words = get_words("views.txt")
    pass_words = ["or", "and", "of", "in","on","at","then", "the", "a", "an", "with", "for"]
    formatted_words = [word.lower() for word in words if word not in pass_words]
    word_count = {word: formatted_words.count(word) for word in formatted_words}
    save_counts(word_count)

def get_words(filename):
    with open(filename,"r") as f:
        content = f.read()
    content = re.sub(r"[^\w\- ]","",content)
    content = re.sub(r"\-\-"," ",content)
    content = content.split()
    return content
    

def save_counts():
    ...

print(get_words("views.txt"))
