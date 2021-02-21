# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:28:16 2021

@author: aarthi
"""

from flask import Flask,render_template,request

import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('loan.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login',methods = ['POST'])
def login():
    #Current Loan Amount
    current = request.form['cla']
    #Term
    term = request.form['t']
    if(term=='Long Term'):
        t1=0
    else:
        t1=1
    #Credit Score
    credit_S = request.form['cr']
    #Annual Income
    annual = request.form['ann']
    #Years in current job
    #global y1,y2,y3,y4,y5,y6,y7,y8,y9,y10
    years = request.form['year']
    #Home Ownership
    global h1,h2,h3,h4
    home = request.form['h']
    if(home=='HaveMortgage'):
        h1,h2,h3,h4=1,0,0,0
    elif(home=='Home Mortgage'):
        h1,h2,h3,h4=0,1,0,0
    elif(home=='Own Home'):
        h1,h2,h3,h4=0,0,1,0
    elif(home=='Rent'):
        h1,h2,h3,h4=0,0,0,1
    #Years of credit history
    yoc = request.form['yoc']
    #Number of credit problems
    num = request.form['noc']
    #Current credit balance
    bal = request.form['ccb']
    #Maximum open credit
    credit = request.form['moc']
    #bakruptacies
    bankrupt = request.form['bank']
    #tax Liens
    tax = request.form['tax']
    sc = StandardScaler()
    total = [[float(current),t1,float(credit_S),float(annual),float(years),h1,h2,h3,h4,float(yoc),float(num),float(bal),float(credit),float(bankrupt),float(tax)]]
    total = sc.fit_transform(total)
    ans = model.predict(sc.transform(total))
    #print(ans[0])
    if(ans[0]=='Charged Off'):
        return render_template("chargedoff.html")
    elif(ans[0]=='Fully Paid'):
        return render_template("fullypaid.html")
if __name__ == '__main__':
    app.run(debug = True)
    
