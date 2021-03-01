#!/mnt/c/Users/adiac/Documents/project/microblog/venv/bin/python
from app import create_app, db
from app.models import User, Post, Task, Notification


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post, 'Notification': Notification, 'Task': Task}


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True)