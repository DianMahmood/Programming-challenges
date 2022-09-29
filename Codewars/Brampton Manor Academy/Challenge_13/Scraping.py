import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"


def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr


def positions(html):
    list_position = []
    i = 0
    position = 0
    while position< 10:
            open_tr = html.find('<tr>', i)
            close_tr = html.find("</tr>", open_tr)
            newstring = html[open_tr:close_tr]
            lookingfor = '"position">'
            pos_start = newstring.find(lookingfor)
            pos_end = newstring.find('</', pos_start)
            i = close_tr
            position += 1
            output = newstring[pos_start + len(lookingfor):pos_end]
            list_position.append(output)
    return list_position



def artists(html):
    list_artist = []
    x = 0
    artist = 0
    while artist < 10:
        open_tr = html.find("<tr>", x)
        close_tr = html.find("</tr>", open_tr)
        newstring = html[open_tr:close_tr]
        lookingfor = '"artist">'
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find("</", pos_start)
        x = close_tr
        artist += 1
        entire = newstring[pos_start:pos_end]
        singer = entire.partition('/">')[2]
        list_artist.append(singer)
    return list_artist


def songs(html):
    list_song = []
    i = 0
    song = 0
    while song < 10:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)
        newstring = html[open_tr:close_tr]
        lookingfor = '"title">'
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find('</', pos_start)
        i = close_tr
        song += 1
        entire = (newstring[pos_start:pos_end])
        music = entire.partition('/">')[2]
        list_song.append(music)
    return list_song


if __name__ == "__main__":
    html = scrape(url)

    print(f"""{'Position':^30}|{'Artist':^30}|{'Song':^30}|
#############################################################################################
""")
    for x in range(0, 10):
        print(f"""{positions(html)[x]:^29}{artists(html)[x]:^32}{songs(html)[x]:^35}
------------------------------|------------------------------|------------------------------|""")
