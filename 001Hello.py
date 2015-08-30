# -*- coding: utf-8 -*-
'''

@ref http://dormousehole.readthedocs.org/en/latest/quickstart.html#id2
'''
from __future__ import unicode_literals, division, with_statement, print_function
__author__ = "Chui-Wen Chiu"

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, url_for, render_template, abort, redirect, make_response, session, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/xyz') # URL 與 Method 對應
def yyy():
    return 'Hello City Hunter'
    
@app.route('/user/<username>') # URL 參數映射到 Method 參數
def show_user_profile(username):
    # show the user profile for that user
    return 'User {0}'.format(username)

@app.route('/post/<int:post_id>') # 限定參數型別為 int
def show_post(post_id):    
    return 'Post {0}'.format( post_id )
    
@app.route('/login', methods=['GET', 'POST']) # 定義可 Handle GET/POST
def login():
    if request.method == 'POST':
        session['username'] = request.form['username'] # 處理 POST 參數
        return redirect(url_for('yyy'))
    else:
        return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>'''

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
    
@app.route('/test1')
def test1():
    abort(401)
    # 執行中止, 以下不會執行
    
@app.route('/test2')
def test2():
    redirect(url_for('hello'))
    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
    
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['X-Something'] = 'A value' # 自訂 Header
    return resp
    
if __name__ == '__main__':
    # 設置密鑰，複雜一點, 可用 os.urandom(24) 產生
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    
    app.debug = True # 除錯模式
    
    app.logger.debug('App Start #1') # 除錯資訊
    # 指定 host
    app.run(host='0.0.0.0', debug = True)