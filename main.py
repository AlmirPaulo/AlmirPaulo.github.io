from browser import document as doc
from browser import html 
from browser.template import Template

#Title and Text
title = html.H1("Front-End, Bots, Scraping and Crawlers (Ethical) development")
#text = html.P({text}, id='text')

#Change language
br_btn = html.INPUT(id='br', type='checkbox')
en_btn = html.INPUT(id='en', type='checkbox')
label_br = html.LABEL(For='br')
label_en = html.LABEL(For='en')
br_flag = html.IMG(src='brazil.png')
us_flag = html.IMG(src='united-states.png')

label_br <= br_flag
label_en <= us_flag


main = html.MAIN()

main <= title + label_br + label_en + br_btn + en_btn 

doc["body"] <= main