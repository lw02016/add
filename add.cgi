#!/usr/bin/python3.6
import cgi
import cgitb
from http import cookies

#日本語を処理するのに必要
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#デバッグ機能を有効にする
cgitb.enable()

#フォーム情報の取り込み
form = cgi.FieldStorage()

#フォームの表示
if form["event"].value == "add":
	if len(form) == 0:
	    CC=""
	    C=""
	else:
	    CC=form["name"].value
	    event=form["event"].value
    	C = cookies.SimpleCookie()
	    C["name"] = CC

print("Content-type: text/html;\n\n")
print("<hr>入力内容<br>")
#フォームの内容を表示
print(f'名前：<b>',CC,"</b><br>")
print(C)
print("</body></html>\n")
