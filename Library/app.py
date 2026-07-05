from flask import Flask, render_template, request, redirect

app = Flask(__name__)

books = []

@app.route('/')
def home():
    return render_template("index.html", books=books)

@app.route('/add', methods=['POST'])
def add():
    book = {
        "id": request.form['bookid'],
        "name": request.form['bookname'],
        "author": request.form['author'],
        "category": request.form['category'],
        "availability": request.form['availability'],
        "description": request.form['description']
    }
    books.append(book)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    bookid = request.form['bookid']
    global books
    books = [b for b in books if b['id'] != bookid]
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)