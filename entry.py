#coding=utf8

import web
import views
import admin

web.config.debug = False

urls = (
    '/(.*)/',views.Redirect,
    '/',views.Index,
    '/category/(.*)',views.Category,
    '/detail/(.*)',views.Detail,
    '/login',admin.Login,
    '/admin',admin.Admin,
    '/category/add',admin.Category_Add,
    '/category/edit',admin.Category_Edit,
    '/category/del',admin.Category_Del,
    '/detail/add',admin.Detail_Add,
    '/detail/edit',admin.Detail_Edit,
    '/detail/del',admin.Detail_Del
)

app = web.application(urls,globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'isLogin': 0})

def session_hook():
    web.ctx.session = session
    
app.add_processor(web.loadhook(session_hook))

if __name__ == '__main__':
    app.run()