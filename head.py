from browser import document as doc 
from browser import html

topicos = ['teste1', 'teste2','Contact']

btn = html.LABEL(For="toggle", Class="toggle") 
btn <= html.IMG(src="list.png")

wrapper = html.DIV(Class="wrapper")
nav = html.NAV()
control = html.DIV(Class="control")
menu =  html.DIV(Class="menu")
list = html.UL()
for i in topicos:
    items = html.LI(i)
    items <= html.A(href='#'+i)
    list <= items

menu <= list
control <= menu
nav <= control
wrapper <= nav

doc["body"] <= html.INPUT(id="toggle", type="checkbox") + btn + wrapper
  