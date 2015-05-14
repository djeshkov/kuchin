#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
import time

from flask import Flask, render_template, request, jsonify, Response, json
import json

import string
import random


#!/usr/bin/python
# -*- coding: utf-8 -*-


import threading
import time



A = None
B = None
M1 = None
M2 = None
F1 = None
F2 = None
F3 = None
F4 = None
F5 = None
F6 = None
F7 = None

event = threading.Event()
F0_done = threading.Event()
F1_done = threading.Event()
F2_done = threading.Event()
F3_done = threading.Event()
F4_done = threading.Event()
F5_done = threading.Event()
F6_done = threading.Event()
F7_done = threading.Event()

list = [ False, False, False, False, False, False, False, False, False ]

flag = False



def genArr(n):
 global M1,M2
 list[0]=True
 M1 = [1 for i in range(n)]
 M2 = [100 for i in range(n)]
 print "Generating Array"
 time.sleep(5)
 F0_done.set()
 list[0]=False

def f1(M1,M2):
 global F1
 list[1]=True
 F1=M1+M2
 print "F1 is on the run"
 time.sleep(5)
 F1_done.set()
 list[1]=False

def f2(M1,M2):
 global F2
 list[2]=True
 F2=M2+M1
 print "F2 is on the run"
 time.sleep(5)
 list[2]=False
 F2_done.set()



def f3(F1):
 F1_done.wait()
 print "F1 is done, starting F3"
 global F3
 list[3]=True
 F3=F1+F1
 time.sleep(5)
 F3_done.set()
 list[3]=False
def f4(F2):
 print "F2 is done, starting F4"
 list[4]=True
 F2_done.wait()
 global F4
 F4=F2+F2
 time.sleep(5)

 list[4]=False
 F4_done.set()

def f5(F2,F4):
 print "starting F5"
 list[5]=True
 global F5
 F5=F2+F4
 time.sleep(2)
 list[5]=False
 F5_done.set()

def f6(F2,F4):
 print "starting F6"
 list[6]=True
 global F6
 F6=F2+F4
 time.sleep(2)
 list[6]=False
 F6_done.set()

def f7(F2,F4):
 print "starting F7"
 list[7]=True
 global F7
 F7=F2+F4
 time.sleep(5)
 F7_done.set()
 list[7]=False

def run():
	flag = True
	F0_done.clear()
	F1_done.clear()
	F2_done.clear()
	F3_done.clear()
	F4_done.clear()
	F5_done.clear()
	F6_done.clear()
	F7_done.clear()

        tf0 = threading.Thread(target=genArr, name="f0", args=[1])

        print "Waiting for Array to be generated"

        tf0.start()
        F0_done.wait()
        tf1 = threading.Thread(target=f1, name="f1", args=[M1,M2])
        tf2 = threading.Thread(target=f2, name="f2", args=[M1,M2])
        tf1.start()
        tf2.start()
        F1_done.wait()
        F2_done.wait()
        tf3 = threading.Thread(target=f3, name="f3", args=[F1])
        tf3.start()
        tf4 = threading.Thread(target=f4, name="f4", args=[F2])
        tf4.start()
        F3_done.wait()
        F4_done.wait()
        tf5 = threading.Thread(target=f5, name="f5", args=[F3,F4])
        tf5.start()
        tf6 = threading.Thread(target=f6, name="f6", args=[F3,F4])
        tf6.start()
        tf7 = threading.Thread(target=f7, name="f7", args=[F3,F4])
        tf7.start()
        F5_done.wait()
        F6_done.wait()
        F7_done.wait()
	list[8]=True
	time.sleep(5)
        F8=F5+F6+F7
	list[8]=False
	flag = False








app = Flask(__name__)


@app.route('/run')
def runtr():
    #if flag is not set, run
    if not flag:
     fr = threading.Thread(target=run, name="run")
     fr.start()
     return 'ok'
    return 'Process is on the run'





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_get_letters')
def letter_replace():
    alphabet = string.ascii_lowercase
    data = list(request.args.get('dataset', alphabet,type=str))
    replace = request.args.get('replace', 3, type=int)

    indices = range(len(data))
    random.shuffle(indices)
    for index in indices[:replace]:
        data[index] = alphabet[int(random.random() * 25)]
    return jsonify(result=''.join(data))
    #return jsonify(result=''.join(data))

@app.route('/_get_data')
def threads_status():


    return Response(json.dumps(list),  mimetype='application/json')
    #return Response(json.dumps(list),  mimetype='application/json')



if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8000"),
        debug=True
    )
