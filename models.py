#coding=utf8

from database import db

class Menu:
    name =''
    slug =''
    def __init__(self,name,slug):
        self.name = name
        self.slug = slug
    
    def __repr__(self):
        return '<Menu:name-%s slug-%s>' % (self.name,self.slug)

class Details:
    id = 0
    title = ''
    content = ''
    def __init__(self,id,title,content):
        self.id = id
        self.title = title
        self.content = content
    
class Shows:
    img = ''
    content = ''
    def __init__(self,img,content):
        self.img = img
        self.content = content
        
def Get_Menu():
    rmenus = db.select('categories',where='parent = 0',order='order_id')
    menus = []
    for menu in rmenus:
        menus += [Menu(menu.name,menu.slug)]
    
    return menus

#根据分类ID获取数据
def Get_Entities(cate_id,_limit):
    rentities = db.select('details',where='cate_id = %d' % int(cate_id,10),limit = int(_limit,10))
    entities = []
    for e in rentities:
        entities += [Details(e.id,e.title,e.content)]
    return entities

def Get_Shows():
    rshows = db.select('shows')
    shows = []
    for s in rshows:
        shows += [Shows(s.img,s.content)]
    return shows