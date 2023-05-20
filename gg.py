from flask import Flask, render_template, request
import os

folder = os.getcwd()
print("рабочая папка тута ===========>", folder)

app  = Flask(__name__ , template_folder=folder)

@app.route('/')
def start():
    return render_template('templates/vvod.html')

@app.route('/login', methods=['POST', 'GET'])
def end():
    return render_template('templates/vivod.html')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    return render_template('templates/redbull.html')

@app.route('/logout1', methods=['POST', 'GET'])
def logout1():
    return render_template('templates/monster.html')

@app.route('/logout2', methods=['POST', 'GET'])
def logout2():
    return render_template('templates/adrenalin.html')

@app.route('/logout3', methods=['POST', 'GET'])
def logout3():
    return render_template('templates/tornado.html')

@app.route('/logout4', methods=['POST', 'GET'])
def logout4():
    return render_template('templates/burn.html')

app.run()

