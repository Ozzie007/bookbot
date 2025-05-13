def get_book_text(file_path):
    text = None
    with open(file_path) as f:
        text = f.read()
    return text

def get_wordcount(txt):
    return len(txt.split())

def get_character_count(txt):
    char_count = {}
    txt = txt.lower()
    for l in txt:
        if l in char_count:
            char_count[l] += 1
        else:
            char_count[l] = 1
    return char_count