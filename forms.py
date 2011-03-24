#coding=utf8

from web import form

form_login = form.Form(
    form.Textbox('name',description=u'用户：'),
    form.Password('password',description=u'密码：')
)