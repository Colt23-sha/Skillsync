from database import create_projects_table
from database import get_db_connection
from flask import Flask, render_template, request , redirect,url_for

app = Flask(__name__)
create_projects_table()


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/skills')
def skills():
    return render_template('skills.html')
@app.route('/delete/<int:id>',methods=['POST'])
def delete_project(id):
    conn=get_db_connection()
    conn.execute('DELETE FROM projects WHERE id=?',(id,))
    conn.commit()
    conn.close()
    return redirect(url_for('project_page'))
@app.route('/projects', methods=['GET','POST'])
def project_page():
    conn = get_db_connection()

    if request.method=='POST':
        title = request.form['title']
        description = request.form['description']
        tech=request.form['tech']
        conn.execute('INSERT INTO projects (title, description, tech) VALUES (?, ?, ?)', (title, description, tech))
        conn.commit()
        conn.close()
        return redirect(url_for('project_page'))
    projects = conn.execute('SELECT * FROM projects').fetchall()
    conn.close()
    return render_template('projects.html', projects=projects)
@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit_project(id):
    conn=get_db_connection()

    if request.method=='POST':
        title=request.form['title']
        description=request.form['description']
        tech=request.form['tech']

        conn.execute('UPDATE projects SET title=?, description=?, tech=? WHERE id=?',(title,description,tech,id))
        conn.commit()
        conn.close()
        return redirect(url_for('project_page'))
    project=conn.execute('SELECT * FROM projects WHERE id=?',(id,)).fetchone()
    conn.close()
    return render_template('edit_project.html',project=project)


if __name__ == "__main__":
    app.run(debug=True)

    