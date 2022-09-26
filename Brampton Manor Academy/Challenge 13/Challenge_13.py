import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"


def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr


def positions(html):
    i = 0
    end = html.find("CENTRAL CEE")
    while i < end:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)
        newstring = html[open_tr:close_tr]
        lookingfor = '"position">'
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find('</', pos_start)
        i = close_tr
        print(newstring[pos_start+len(lookingfor):pos_end])


#def artists(html):
    #open_tr = html.find('<tr>', i)
    #close_tr = html.find("</tr>", open_tr)

    #newstring = html[open_tr:close_tr]
    #lookingfor = '"artist">'
    #pos_start = newstring.find(lookingfor)
    #pos_end = newstring.find('</', pos_start)
    #print(newstring[pos_start + len(lookingfor):pos_end])



    
    #return newstring[pos_start+len(lookingfor):pos_end]

if __name__ == "__main__":
    html = scrape(url)
    positions(html)
    open_tr = html.find('<tr>')
    close_tr = html.find("</tr>", open_tr)
    newstring = html[open_tr:close_tr]
    lookingfor = '"artist">'
    pos_start = newstring.find(lookingfor)
    pos_end = newstring.find('</', pos_start)
    print(newstring[pos_start + len(lookingfor):pos_end])
