def main():
    user = input("Input: ")
    print("Output:", short_version(user))

def short_version(text):
    text = text.strip()
    vowels = "aeiouAEIOU"
    text_no_vowels = ""
    for c in text:
        if c not in vowels:
            text_no_vowels += c
    return text_no_vowels
main()
