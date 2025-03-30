"""
Note: the path of current working directory and script directory are usually not the same.
 --> CWD (current working directory) is the directory where python script is executed from.
 --> Script directory is the directory where script file (.py) is located, regardless of where it is exectued from

.split() works with strings, but returns a list of strings.
re.sub() works with strings and returns strings
"""

import re
import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
text_path = os.path.join(script_dir, "views.txt")
save_counts_path = os.path.join(script_dir, "counts.csv")

def main():
    word_count = {}
    words = get_words(text_path)
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
    


def save_counts(counts):
    with open(save_counts_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Word", "Count"])
        for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([word, count])

# main()
print(get_words(text_path))
