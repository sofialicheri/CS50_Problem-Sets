import requests
import sys
import emoji

user = ""

def main():
    user = input("Input: ")
    print(alias(user))

def alias(face):
    converted_emoji = emoji.emojize(face)
    converted_emoji = emoji.emojize(face, language='alias')
    return converted_emoji

main()
