from blog import app, db
from blog.models import User, Post, Folder, Cit


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Folder': Folder, 'Cit': Cit}