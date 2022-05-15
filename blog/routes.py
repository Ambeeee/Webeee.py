from click import password_option
from flask import abort, request, flash, redirect, render_template, url_for
import flask
from flask_login import current_user, login_user, logout_user, login_required

from blog import app, db
from blog.forms import LoginForm, SubscribeForm, PostForm, FolderForm, CitaForm
from blog.models import Post, User, Folder, Cit
from blog.utils import title_slugifier, save_picture
from blog.permissions import BOSS, WRITER, CIT

#HOME
@app.route("/")
def homepage():
    return render_template("homepage.html")





#LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('username e password non combaciano!')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('homepage'))
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('homepage'))





#NEWS
@app.route("/newsPres")
def newsPres():
    page_number = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.created_at.desc()).paginate(page_number, 50, True)
    if posts.has_next:
        next_page = url_for('newsPres', page=posts.next_num)
    else:
        next_page = None

    if posts.has_prev:
        previous_page = url_for('newsPres', page=posts.prev_num)
    else:
        previous_page = None
    return render_template("newsPres.html", posts=posts, current_page=page_number, next_page=next_page, previous_page=previous_page)

@app.route("/posts/<string:post_slug>")
def post_detail(post_slug):
    post_instance = Post.query.filter_by(slug=post_slug).first_or_404()
    return render_template("post_detail.html", post=post_instance)

@app.route("/posts/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def post_update(post_id):   
    post_instance = Post.query.get_or_404(post_id)
    if post_instance.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post_instance.title = form.title.data
        post_instance.description = form.description.data
        post_instance.body = form.body.data

        if form.cover.data:
            try:
                cover = save_picture(form.cover.data)
                post_instance.image = cover
            except Exception:
                db.session.commit()
                flash("C'è stato un problema con l'upload dell'immagine. Cambia immagine e riprova")
                return redirect(url_for('post_update', post_id=post_instance.id))

        db.session.commit()
        return redirect(url_for('post_detail', post_slug=post_instance.slug))
    elif request.method == "GET":
        form.title.data = post_instance.title
        form.description.data = post_instance.description
        form.body.data = post_instance.body
        cover = post_instance.image or None
    return render_template("post_editor.html", form=form, post_cover=cover)

@app.route("/posts/<int:post_id>/delete", methods=["POST"])
@login_required
def post_delete(post_id):
    post_instance = Post.query.get_or_404(post_id)
    if post_instance.author != current_user:
        abort(403)
    db.session.delete(post_instance)
    db.session.commit()
    return redirect(url_for('newsPres'))





#GALLERY
@app.route("/gallery")
def gallery():
    page_number = request.args.get('page', 1, type=int)
    folders = Folder.query.order_by(Folder.created_at.desc()).paginate(page_number, 50, True)
    if folders.has_next:
        next_page = url_for('gallery', page=folders.next_num)
    else:
        next_page = None

    if folders.has_prev:
        previous_page = url_for('gallery', page=folders.prev_num)
    else:
        previous_page = None
    return render_template("gallery.html", folders=folders, current_page=page_number, next_page=next_page, previous_page=previous_page)

@app.route("/gallery/<string:post_slug>")
def album(post_slug):
    folder_instance = Folder.query.filter_by(slug=post_slug).first_or_404()
    return render_template("album.html", folders=folder_instance)







#WIKIPRES
@app.route("/citazionis")
def cit():
    page_number = request.args.get('page', 1, type=int)
    cits = Cit.query.order_by(Cit.created_at.desc()).paginate(page_number, 50, True)
    if cits.has_next:
        next_page = url_for('cit', page=cits.next_num)
    else:
        next_page = None

    if cits.has_prev:
        previous_page = url_for('cit', page=cits.prev_num)
    else:
        previous_page = None
    return render_template("cit.html", cits=cits, current_page=page_number, next_page=next_page, previous_page=previous_page)

@app.route("/cit/<int:cit_id>/delete", methods=["POST"])
@login_required
def cit_delete(cit_id):
    cit_instance = Cit.query.get_or_404(cit_id)
    if cit_instance.author != current_user:
        abort(403)
    db.session.delete(cit_instance)
    db.session.commit()
    return redirect(url_for('cit'))

@app.route("/cit/<int:cit_id>/update", methods=["GET", "POST"])
@login_required
def cit_update(cit_id):
    cit_instance = Cit.query.get_or_404(cit_id)
    if cit_instance.author != current_user:
        abort(403)
    form = CitaForm()
    if form.validate_on_submit():
        cit_instance.body = form.body.data

        db.session.commit()
        return redirect(url_for('cit', post_slug=cit_instance.slug))
    elif request.method == "GET":
        form.body.data = cit_instance.body
    return render_template("post_editor.html", form=form)






#CREA
@app.route("/crea")
def crea():
    return render_template("crea.html")

@app.route("/create-post", methods=["GET", "POST"])
@login_required
def post_create():
    form = PostForm()
    if form.validate_on_submit():
        slug = title_slugifier(form.title.data)
        new_post = Post(title=form.title.data,
            description=form.description.data, body=form.body.data,
            body2=form.body2.data, body3=form.body3.data, body4=form.body4.data, body5=form.body5.data,
            cit=form.cit.data, cit2=form.cit2.data, cit3=form.cit3.data, 
            slug=slug, author=current_user)

        if form.cover.data:
            try:
                cover = save_picture(form.cover.data)
                new_post.image = cover
            except Exception:
                db.session.add(new_post)
                db.session.commit()
                flash("C'è stato un problema con l'upload dell'immagine. Cambia immagine e riprova")
                return redirect(url_for('post_update', post_id=new_post.id))

        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("post_detail", post_slug=slug))
    return render_template("post_editor.html", form=form)

@app.route("/create-folder", methods=["GET", "POST"])
@login_required
def folder_create():
    form = FolderForm()
    if form.validate_on_submit():
        slug = title_slugifier(form.title.data)
        new_folder = Folder(title=form.title.data, description=form.description.data, slug=slug, author=current_user)

        if form.cover.data:
            try:
                cover = save_picture(form.cover.data)
                new_folder.cover = cover
            except Exception:
                db.session.add(new_folder)
                db.session.commit()
                flash("C'è stato un problema con l'upload dell'immagine. Cambia immagine e riprova")
                return redirect(url_for('post_update', post_id=new_folder.id))
        if form.media.data:
            try:
                media = save_picture(form.media.data)
                new_folder.media = media
            except Exception:
                db.session.add(new_folder)
                db.session.commit()
                flash("C'è stato un problema con l'upload dell'immagine. Cambia immagine e riprova")
                return redirect(url_for('post_update', post_id=new_folder.id))

        db.session.add(new_folder)
        db.session.commit()
        return redirect(url_for("album", post_slug=slug))
    return render_template("post_editor.html", form=form)

@app.route("/create-cit", methods=["GET", "POST"])
@login_required
def cit_create():
    form = CitaForm()
    if form.validate_on_submit():
        slug = title_slugifier(form.body.data)
        new_cit = Cit(body=form.body.data, slug=slug, author=current_user)

        db.session.add(new_cit)
        db.session.commit()
        return redirect(url_for("cit", post_slug=slug))
    return render_template("post_editor.html", form=form)

@app.route("/create-user", methods=["GET", "POST"])
@login_required
def user_create():
    form = SubscribeForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role=form.role.data)
        new_user.set_password_hash(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("post_editor.html", form=form)






