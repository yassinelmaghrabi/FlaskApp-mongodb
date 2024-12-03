from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://root:example@mongodb:27017") 
db = client["user_database"]  
collection = db["user_data"]  

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        

        collection.insert_one({"name": name, "email": email, "age": age})
        return redirect('/view')
    
    return render_template('index.html')

@app.route('/view')
def view_data():

    data = collection.find()
    return render_template('view.html', data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
