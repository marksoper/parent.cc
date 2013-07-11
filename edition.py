
import sys
import markdown
import json

dirname = sys.argv[1].rstrip("/")

articleNamesFile = open(dirname + "/edition.json", "r")
articles = json.loads(articleNamesFile.read())
articleNamesFile.close()

articlesHtml = []
for article in articles:
    mdfile = open(dirname + "/" + article, "r")
    md = mdfile.read()
    mdfile.close()
    html = markdown.markdown(md)
    articlesHtml.append(html)

delim = "\n\n\n"
html = delim + delim.join(articlesHtml) + delim

htmlFile = open(dirname + "/" + dirname + ".html", "w")
htmlFile.write(html)
htmlFile.close()