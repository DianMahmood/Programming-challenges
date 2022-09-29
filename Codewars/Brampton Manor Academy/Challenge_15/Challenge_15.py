import csv


def read_csv(path):
    csv_content = []
    with open(path) as file:
        csvreader = csv.reader(file, delimiter=",")
        for row in csvreader:
            csv_content.append(row)
        return csv_content


def read_html(path):
    file = open(path)
    return file.read()


def initials(csv, html):
    i = 0
    initials_list = []
    number = 0
    while number < 5:
        for y in range(0, 5):
            text = read_csv(csv)
            file = read_html(html)
            open_h2 = file.find("<h2", i)
            close_h2 = file.find("/h2", open_h2)
            newstring = file[open_h2:close_h2]
            lookingfor = 'class="el__heading">'
            pos_start = newstring.find(lookingfor)
            pos_end = newstring.find("<", pos_start)
            x = newstring[pos_start+len(lookingfor):pos_end]
            replace = text[y][1]
            new = x.replace(x, replace)
            initials_list.append(new)
            i = close_h2
            number += 1
    return initials_list


text = "south.csv"
web = "south.html"
print(initials(text, web))

