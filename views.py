#coding=utf8

import web
from web.contrib.template import render_jinja
from models import Get_Menu,Get_Shows

render = render_jinja(
    'templates',
    encoding = 'utf8',
)


class Redirect:
    def GET(self,path):
        web.seeother('/'+path)
        
class Index:
    def GET(self):
        m = Get_Menu()
        s = Get_Shows()
        return render.index(m=m,s=s)
    
class Category:
    def GET(self,id):
        return 'category %s' % int(id,10)

class Detail:
    def GET(self,id):
        return 'detail-%d' % int(id,10)