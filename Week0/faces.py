def main():
    user = input()
    print(converted(user))

def converted(text):
    smiley = ":)"
    if ":)" in text:
        text = text.replace(":)","🙂")
    if ":(" in text:
        text = text.replace(":(","🙁")
    return text
main()
