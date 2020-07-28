from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__) # Crée un instance de la classe Flask, c'est notre app
app.config.from_object('config')

# MODEL

db = SQLAlchemy(app) # Lie notre app à SQLAlchemy

class Task(db.Model): # Modèle
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

db.create_all()

# VIEWS

@app.route('/', methods=['GET', 'POST']) 
def index(): # Méthode appelée lorsqu'on se rend sur la route '/'
    if request.method == 'POST':
        name = request.form.get('name')
        task = Task(name=name)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        tasks = Task.query.order_by(Task.created_at).all()
    return render_template('index.html', tasks=tasks)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.name = request.form.get('name')
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('update.html', task=task)

@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))
