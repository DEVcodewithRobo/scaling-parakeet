from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database="SURVEY"  # Replace with your database name
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    phone = request.form['phone']
    review = request.form['review']

    # Extracting answers for each audio MCQ
    mcq_answers = []
    for i in range(1, 8):
        mcq_answers.append(request.form[f'a{i}'])

    cursor = mydb.cursor()
    sql = "INSERT INTO form (name, email, age, phone, a1, a2, a3, a4, a5, a6, a7, review) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (name, email, age, phone) + tuple(mcq_answers) + (review,)
    cursor.execute(sql, val)
    mydb.commit()

    return "Survey submitted successfully!"

if __name__ == '__main__':
    app.run(debug=False)
