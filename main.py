from browser import document as doc
from browser import html 

title = html.H1("Front-End, Bots, Scraping and Crawlers (Ethical) development")
text = html.P("Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque veritatis nemo magnam consectetur laborum repellat nobis recusandae, rem exercitationem inventore enim aperiam qui deserunt aut distinctio tempora itaque dicta similique?")
main = html.MAIN()

main <= title + text 

doc["body"] <= main