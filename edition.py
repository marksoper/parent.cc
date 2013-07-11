
import sys
import markdown
import json
import codecs

dirname = sys.argv[1].rstrip("/")

articleNamesFile = open(dirname + "/edition.json", "r")
articles = json.loads(articleNamesFile.read())
articleNamesFile.close()

articlesHtml = []
for article in articles:
    #mdfile = open(dirname + "/" + article, "r")
    mdfile = codecs.open(dirname + "/" + article, mode="r", encoding="utf-8")
    #md = unicode(mdfile.read(), errors="replace")
    md = mdfile.read()
    mdfile.close()
    html = markdown.markdown(md)
    articlesHtml.append(html)

delim = "\n\n\n"
html = delim + delim.join(articlesHtml) + delim

#htmlFile = open(dirname + "/" + dirname + ".html", "w")

htmlFile = codecs.open(dirname + "/" + dirname + ".html",
	"w",
	encoding="utf-8", 
    errors="xmlcharrefreplace"
)

htmlFile.write(html)
htmlFile.close()

