# encoding=utf-8
from flask import Flask, render_template, Response, request
from megapi import *

app = Flask(__name__)

#设置全局变量
g_data = None
def onRead(data):
    global g_data
    g_data = data
    print g_data

# Megapi 驱动初始化
bot = MegaPi()
bot.start('/dev/ttyUSB0')

#返回index.html页面
@app.route('/')
def index():
    return render_template("index.html")

#获取传感器最新值
@app.route('/read')
def onReadReq():
    bot.soundSensorRead(7,onRead)
    return str(g_data )
    print str(g_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False ,threaded=True,port=8888)