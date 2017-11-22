from flask import render_template, request
from models import Category, MYTodo, Priority, db
from my_todoapp import app

 
# @app.route('/')
# def index():
# 	return '<h1>aahh edichavu le!</h1>'

@app.route('/')

def list_all():
   return render_template(
       'list.html',
       categories=Category.query.all(),
       todos=Todo.query.join(Priority).order_by(Priority.value.desc())
@app.route('/new-task', methods=['POST'])
def new():
   if request.method == 'POST':
       category = Category.query.filter_by(id=request.form['category']).first()
       priority = Priority.query.filter_by(id=request.form['priority']).first()
       todo = Todo(category, priority, request.form['description'])
       db.session.add(todo)
       db.session.commit()
       return redirect('/')
   else:
       return render_template(
           'new-task.html',
           page='new-task',
           categories=Category.query.all(),
           priorities=Priority.query.all()
       )
