from bs4 import BeautifulSoup
data='''
    <html>
    <head>
    <title>First Demo</title>
    </head>
    <body>
    <h1 class="heading1">Hello Srini</h1>
    <h1 class="heading2">Hello Harsha</h1>
    <h1 class="heading1">Hello Abillash</h1>
    <h1 class="heading2">Hello Yuvraj</h1>
    </body>
    </html>
    '''
text = []
soup = BeautifulSoup(data,'lxml')
h1s=soup.find_all("h1", {"class": "heading1"})
for h1 in h1s:
    text.append(h1.get_text())
    print(h1.get_text())
