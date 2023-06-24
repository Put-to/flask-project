from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",
    database="words"
)


@app.route('/')
def get_word():
    cursor = db.cursor()
    cursor.execute("SELECT word FROM word LIMIT 1")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return "No word found in the database."


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        new_word = request.form['new_word']
        cursor = db.cursor()
        cursor.execute("UPDATE word SET word = %s", (new_word,))
        db.commit()
    return render_template('admin.html')


if __name__ == '__main__':
    app.run()
