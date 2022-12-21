import sys
import os

# write your code here
# write your code here
# print("""# John Lennon
# or ***John Winston Ono Lennon*** was one of *The Beatles*.
# Here are the songs he wrote I like the most:
# - Imagine
# - Norwegian Wood
# - Come Together
# - In My Life
# - ~~Hey Jude~~ (that was *McCartney*)""")

available_formats = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list",
                     "new-line"]
special_comands = ["!help", "!done"]
text = """"""


def plain():
    global text
    text = text + input("Text: ")
    print(text)


def bold():
    global text
    entered = input("Text: ")
    text = text + "**" + entered + "**"
    print(text)


def italic():
    global text
    entered = input("Text: ")
    text = text + "*" + entered + "*"
    print(text)


def inline():
    global text
    entered = input("Text: ")
    text = text + "`" + entered + "`"
    print(text)


def link():
    global text
    entered = input("Label: ")
    text = text + "[" + entered + "]"
    entered = input("URL: ")
    text = text + "(" + entered + ")"
    print(text)


def header():
    global text
    entered = int(input("Level: "))
    if 0 < entered < 7:
        text = text + "#" * entered
        entered = input("Text: ")
        text = text + " " + entered + "\n"
        print(text)
    else:
        print("The level should be within the range of 1 to 6")
        header()


def new_line():
    global text
    text = text + "\n"
    print(text)


def add_list(e_text):
    global text
    entered = int(input("Number of rows: "))
    if entered < 1:
        print("The number of rows should be greater than zero")
        add_list(e_text)
    else:
        li = list(
            map(lambda i: str(i + 1) + ". " + input(
                f"Row #{i + 1}: ") + "\n" if e_text == "ordered-list" else "* " + input(
                f"Row #{i + 1}: ") + "\n", range(entered)))
        text = text + "".join(li)
        print(text)


def get_input():
    global text
    entered_text = input("Choose a formatter: ")
    if entered_text in available_formats:
        if entered_text == "plain":
            plain()
        elif entered_text == "bold":
            bold()
        elif entered_text == "italic":
            italic()
        elif entered_text == "inline-code":
            inline()
        elif entered_text == "link":
            link()
        elif entered_text == "header":
            header()
        elif entered_text == "new-line":
            new_line()
        elif entered_text.endswith("-list"):
            add_list(entered_text)
        get_input()
    elif entered_text == "!help":
        print("""Available formatters: plain bold italic header link inline-code new-line ordered-list unordered-list
        Special commands: !help !done""")
        get_input()
    elif entered_text == "!done":
        with open(f"{os.getcwd()}/output.md", 'w') as file:
            # text = text+"\n"
            file.write(text)
        sys.exit()
    else:
        print("Unknown formatting type or command")
        get_input()


get_input()
