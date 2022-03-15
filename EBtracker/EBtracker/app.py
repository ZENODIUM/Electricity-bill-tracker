from flask import Flask, render_template,request,session, redirect,url_for
import os

import sqlite3

app = Flask(__name__)
app.secret_key="123"
graph_name = ""
pass_word = ""

@app.route("/")
def mainpage():
    return render_template('pre.html')

@app.route('/mains',methods=["GET","POST"])
def mains():
    energy = 0
    tv_cost = 0
    fridge_cost = 0
    wm_cost = 0
    ac_cost = 0
    pc_cost = 0
    wh_cost = 0
    tl_cost = 0
    cf_cost = 0
    mo_cost = 0
    pr_cost = 0

    def calculate(units):
        if (units < 100):
            return 0
        elif (units <= 200):
            return ((units - 100)*1.5)+20
        elif (units <= 500):
            return (100*2 + (units - 200)*3) + 20
        elif (units > 500):
            return (100*3.5 + 300*4.6 + (units - 500)*6.6)+50
    def calculate_kar(units):
        if (units <= 30):
            return units*3.75
        elif (units<=100):
            return (units*5.2)
        elif (units <= 200):
            return units*6.75
        elif (units>200):
            return units*7.8
    if request.method == "POST":
        devices = request.form.getlist('device')
        name = request.form.get("username")
        password = request.form.get("password")
        month = request.form.get("month")
        state = request.form.get("state")

        tv_quan = int(request.form.get("tv_quan"))if request.form.get("tv_quan") else 0
        tv_time = int(request.form.get("tv_time")) if request.form.get("tv_time") else 0
        tv_watt = int(request.form.get("tv_watt")) if request.form.get("tv_watt") else 0

        fridge_quan = int(request.form.get("fridge_quan")) if request.form.get("fridge_quan") else 0
        fridge_time = int(request.form.get("fridge_time")) if request.form.get("fridge_time") else 0
        fridge_watt = int(request.form.get("fridge_watt")) if request.form.get("fridge_watt") else 0

        wm_quan = int(request.form.get("wm_quan")) if request.form.get("wm_quan") else 0
        wm_time = int(request.form.get("wm_time"))if request.form.get("wm_time") else 0
        wm_watt = int(request.form.get("wm_watt"))if request.form.get("wm_watt") else 0

        ac_quan = int(request.form.get("ac_quan"))if request.form.get("ac_quan") else 0
        ac_time = int(request.form.get("ac_time"))if request.form.get("ac_time") else 0
        ac_watt = int(request.form.get("ac_watt"))if request.form.get("ac_watt") else 0

        pc_quan = int(request.form.get("pc_quan"))if request.form.get("pc_quan") else 0
        pc_time = int(request.form.get("pc_time"))if request.form.get("pc_time") else 0
        pc_watt = int(request.form.get("pc_watt"))if request.form.get("pc_watt") else 0

        wh_quan = int(request.form.get("wh_quan"))if request.form.get("wh_quan") else 0
        wh_time = int(request.form.get("wh_time"))if request.form.get("wh_time") else 0
        wh_watt = int(request.form.get("wh_watt"))if request.form.get("wh_watt") else 0

        tl_quan = int(request.form.get("tl_quan"))if request.form.get("tl_quan") else 0
        tl_time = int(request.form.get("tl_time"))if request.form.get("tl_time") else 0
        tl_watt = int(request.form.get("tl_watt"))if request.form.get("tl_watt") else 0

        cf_quan = int(request.form.get("cf_quan"))if request.form.get("cf_quan") else 0
        cf_time = int(request.form.get("cf_time"))if request.form.get("cf_time") else 0
        cf_watt = int(request.form.get("cf_watt"))if request.form.get("cf_watt") else 0

        mo_quan = int(request.form.get("mo_quan"))if request.form.get("mo_quan") else 0
        mo_time = int(request.form.get("mo_time"))if request.form.get("mo_time") else 0
        mo_watt = int(request.form.get("mo_watt"))if request.form.get("mo_watt") else 0

        pr_quan = int(request.form.get("pr_quan")) if request.form.get("pr_quan") else 0
        pr_time = int(request.form.get("pr_time"))if request.form.get("pr_time") else 0
        pr_watt = int(request.form.get("pr_watt"))if request.form.get("pr_watt") else 0
        energy = 30*(tv_quan*tv_time*tv_watt + fridge_quan*fridge_time*fridge_watt + wm_quan*wm_time*wm_watt + ac_quan*ac_time*ac_watt + pc_quan*pc_time*pc_watt + wh_quan*wh_time*wh_watt + tl_quan*tl_time*tl_watt + cf_quan*cf_time*cf_watt + mo_quan*mo_time*mo_watt + pr_quan*pr_time*pr_watt)/1000
        if state == "Karnataka":
            total_cost = round(calculate_kar(energy),2)
        else:
            total_cost = round(calculate(energy),2)
        tv_cost = tv_quan*tv_time*tv_watt
        fridge_cost = fridge_quan*fridge_time*fridge_watt
        wm_cost = wm_quan*wm_time*wm_watt
        ac_cost = ac_quan*ac_time*ac_watt
        pc_cost = pc_quan*pc_time*pc_watt
        wh_cost = wh_quan*wh_time*wh_watt
        tl_cost = tl_quan*tl_time*tl_watt
        cf_cost = cf_quan*cf_time*cf_watt
        mo_cost = mo_quan*mo_time*mo_watt
        pr_cost = pr_quan*pr_time*pr_watt

        cost = total_cost
        global graph_name
        global pass_word
        graph_name = name
        pass_word = password
        connection = sqlite3.connect("records.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO records (name,password,cost,month)values(?,?,?,?)",(name,password,cost,month))
        data = cursor.fetchall()
        connection.commit()
        print(data)

        return render_template('result.html',name = name,state = state,total_cost = total_cost,devices = devices,wm_cost = wm_cost,tv_cost=tv_cost,fridge_cost=fridge_cost,ac_cost=ac_cost,pc_cost=pc_cost,wh_cost=wh_cost,tl_cost=tl_cost,cf_cost=cf_cost,mo_cost=mo_cost,pr_cost=pr_cost,tv_time=tv_time,tv_watt=tv_watt,fridge_time=fridge_time,fridge_watt=fridge_watt,wm_time=wm_time,wm_watt=wm_watt,ac_time=ac_time,ac_watt=ac_watt,pc_time=pc_time,pc_watt=pc_watt,wh_time=wh_time,wh_watt=wh_watt,tl_time=tl_time,tl_watt=tl_watt,cf_time=cf_time,cf_watt=cf_watt,mo_time=mo_time,mo_watt=mo_watt,pr_time=pr_time,pr_watt=pr_watt,tv_quan=tv_quan,fridge_quan=fridge_quan,wm_quan=wm_quan,ac_quan=ac_quan,pc_quan=pc_quan,wh_quan=wh_quan,tl_quan=tl_quan,cf_quan=cf_quan,mo_quan=mo_quan,pr_quan=pr_quan)


    return render_template('mains.html')
@app.route('/graph',methods=["GET","POST"])
def graph():
    display_name = []
    display_cost = []
    display_month = []
    connection = sqlite3.connect("records.db")
    cursor = connection.cursor()
    cursor.execute("select * from records where name = ? and password = ?",(graph_name,pass_word))
    data1 = cursor.fetchall()
    print(data1)
    for i in data1:
        display_name.append(i[0])
        display_cost.append(i[2])
        display_month.append(i[3])
    print(display_name)
    print(display_cost)
    print(display_month)



    return render_template('graph.html',display_month = display_month,display_cost = display_cost)




if __name__ == '__main__':
    app.run(debug=True)