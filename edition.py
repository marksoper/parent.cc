
import codecs
import markdown
import json

articleNamesFile = open("./28June2013.json", "r")
articles = json.loads(articleNamesFile.read())
articleNamesFile.close()

articlesHtml = []
for article in articles:
    mdfile = open("./" + article, "r")
    md = mdfile.read()
    mdfile.close()
    html = markdown.markdown(md)
    articlesHtml.append(html)

delim = "\n\n\n"
html = delim + delim.join(articlesHtml) + delim

htmlFile = open("./28June2013.html", "w")
htmlFile.write(html)
htmlFile.close()