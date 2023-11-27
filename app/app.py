import sqlite3
from flask import Flask, render_template, send_from_directory,request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    notes = conn.execute('SELECT * FROM notes').fetchall()
    conn.close()
    return render_template('index.html', notes=notes)



@app.route('/' , methods = ['POST','GET'])
def login():
    #get form data
    #check database for username and check if password correct
    # if correct --> redirect page and populate div with notes with uid = users uid
    #else --> rerror
    #return the index page 
    return ""


@app.route('/add_note', methods=['POST','GET'])
def add_note():
    title = request.form.get('note_title')
    description = request.form.get('note_text')
    color = request.form.get('note_color')
    conn = get_db_connection()
    conn.execute("INSERT INTO notes (title, description, color) VALUES (?, ?, ?)",
                 (title, description, color))
    conn.commit()
    conn.close()

    last_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    new_note = conn.execute("SELECT * FROM notes WHERE id = ?", (last_id,)).fetchone()
    conn.close()

    return jsonify({'id': new_note['id'], 'title': new_note['title'], 'description': new_note['description'], 'color': new_note['color']})

@app.route('/delete_note/<int:note_id>', methods=['GET', 'POST'])
def delete_note(note_id):
    conn = get_db_connection()
    # print(note_id)
    noteID = request.form.get('note_id')
    if request.method == 'POST':
        # sql_update_query = """DELETE from notes where id = ?"""
        n = f"DELETE from notes WHERE id = '{note_id}'"
        # conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conn.execute(n)
        # conn.execute(sql_update_query, (noteID,))
        # print(sql_update_query)
        conn.commit()
    conn.close()   
    return index()

@app.route('/edit_note/<int:note_id>', methods=['POST'])
def edit_note(note_id):
    new_title = request.form.get('new_title')
    new_content = request.form.get('new_content')
    conn = get_db_connection()
    conn.execute("UPDATE notes SET title=?, description=? WHERE id=?",
                 (new_title, new_content, note_id))
    conn.commit()
    updated_note = conn.execute("SELECT * FROM notes WHERE id=?", (note_id,)).fetchone()
    conn.commit()
    conn.close()
    return jsonify({'title': updated_note['title'], 'description': updated_note['description']})


@app.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('js',path)




if __name__ == '__main__':
   app.run(debug = True)