#coding=utf8
import web
import forms

class Login:
    def GET(self):
        return forms.form_login.render()
    
    def POST(self):
        return 'login action'

class Login_Required:
    def __init__(self):
        isLogin = web.ctx.session.get('isLogin',0)
        if isLogin == 0:
            raise web.seeother('/login/',absolute=True)

class Admin(Login_Required):
    def GET(self):
        return 'admin index'
    
#category

class Category_Add(Login_Required):
    def GET(self,cate_name):
        return 'category add : %s' % cate_name
    
class Category_Edit(Login_Required):
    def GET(self,id):
        return 'category edit : %d' % int(id,10)
    
    def POST(self):
        return 'category edit action'
    
class Category_Del(Login_Required):
    def GET(self,id):
        return 'category del : %d' % int(id,10)
        
#detail
class Detail_Add(Login_Required):
    def GET(self):
        return 'detail add form'
    
    def POST(self):
        return 'detial add action'
    
class Detail_Edit(Login_Required):
    def GET(self,id):
        return 'detail edit %d' % int(id,10)
    
    def POST(self):
        return 'detail edit action'
    
class Detail_Del(Login_Required):
    def GET(self,id):
        return 'detail delete %d' % int(id,10)
        
#shows
class Shows_Add(Login_Required):
    def GET(self):
        return 'shows add form'
    def POST(self):
        return 'shows add adction'
    
class Shows_Del(Login_Required):
    def GET(self,id):
        return 'shows delete %d' % int(id,10)