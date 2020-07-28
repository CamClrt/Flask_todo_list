"""
    This is an short project to learn how to use Flask from the docstring 
    blog: https://www.docstring.fr/blog/creer-une-todo-app-avec-flask/.
    
    The aim to this project is to create a simple to do list
"""

from todo_app import app

if __name__ == "__main__":
    app.run(debug=True)