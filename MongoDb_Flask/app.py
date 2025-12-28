from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://bathulamadhu99:1qaz2wsx@madhupract.l3mztza.mongodb.net/mydb"
)
db = client["mydb"]
collection = db["users"]

@app.route('/', methods=['GET', 'POST'])
def form():
    error = None
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']

            collection.insert_one({
                "name": name,
                "email": email
            })
            return redirect(url_for('success'))
        except Exception as e:
            error = str(e)

    return render_template('form.html', error=error)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
