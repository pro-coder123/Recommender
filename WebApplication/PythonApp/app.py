import os
from flask import Flask, flash, redirect, render_template, request, session, abort
from models.keras_first_go import KerasFirstGoModel
from clear_bash import clear_bash

app = Flask(__name__)
cleaner=clear_bash()

def train_model():
    global first_go_model

    print("Train the model")
    first_go_model = KerasFirstGoModel()

@app.route("/")
def index():

    return render_template('index.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
#    if request.method == 'POST':
#       result = request.form.getlist('Job')
#       print(result[0])
#       train_model()
#       processed_text = first_go_model.prediction(result[0])
#       result = {'Job': processed_text}
#       return render_template("result.html",result = result)

    if request.method == 'POST':
      result = request.json
      query = ', '.join(map(str, result['skills'])) 
      print(query)
      train_model()
      processed_text = first_go_model.prediction(query)
      result = {'recommendations': processed_text}
      return result
      
      

def clear_bash():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    app.run()
