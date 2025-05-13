from stats import *
import sys

if(len(sys.argv) != 2 ):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

pth = sys.argv[1]
txt = get_book_text(pth)
count = get_wordcount(txt)
char_count = get_character_count(txt)
print("="* 10 + " BOOKBOT " + "="*10)
print(f"Analyzing book found at {pth}...")
print("-"* 10 + " Word Count " + "-"*10)
print(f"Found {count} total words")
print("-"* 10 + " Character Count " + "-"*10)
for character in char_count:
    print(f"{character}: {char_count[character]}")
