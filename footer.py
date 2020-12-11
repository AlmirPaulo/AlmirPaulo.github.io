from browser import document as doc
from browser import html

doc['body'] <= html.FOOTER(id='Contact')
doc['Contact'] <= html.H2('Contact me:')


img_git = html.A(href='https://github.com/AlmirPaulo/' , target='_blank')
img_git <= html.IMG(src='github.png', Class='social-media')
img_linkedin = html.A(href='3', target='_blank')
img_linkedin <= html.IMG(src='linkedin.png', Class='social-media')
img_email =  html.A(href='mailto:ap.freelas@gmail.com') 
img_email <= html.IMG(src='email.png', Class='social-media')
doc['Contact'] <= img_email + img_git + img_linkedin
doc['Contact'] <= html.UL()



    