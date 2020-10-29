#!/mnt/c/Users/adiac/Documents/project/microblog/venv/bin/python
from app import create_app, db
from app.models import User, Role, Permission, Post, Task, Notification, AnonymousUser


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "Role": Role,
        "Permission": Permission,
        "Post": Post,
        "AnonymousUser": AnonymousUser,
        "Notification": Notification,
        "Task": Task,
    }


if __name__ == "__main__":
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)
