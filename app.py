import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Static page routes
@app.route("/get_posts")
def get_posts():
    posts = list(mongo.db.posts.find().limit(15))
    return render_template("forum.html", posts=posts)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contactus', methods=["GET", "POST"])
def contactus():
    if request.method == "POST":
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "comment": request.form.get("comment")
        }
        mongo.db.contactuspage.insert_one(register)
    return render_template('contactus.html')


@app.route('/companies')
def companies():
    return render_template('companies.html')

# Error Handling of 404 & 500


@app.errorhandler(404)
def response_404(exception):
    return render_template('404.html', exception=exception)


@app.errorhandler(500)
def response_500(exception):
    return render_template('500.html', exception=exception)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    posts = list(mongo.db.posts.find({"$text": {"$search": query}}))
    return render_template("forum.html", posts=posts)


@app.route("/joinus", methods=["GET", "POST"])
def joinus():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("joinus"))

        register = {
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "email": request.form.get("email"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["username"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("get_posts"))

    return render_template("joinus.html")


@app.route("/registercompany", methods=["GET", "POST"])
def registercompany():
    if request.method == "POST":
        register = {
            "companyname": request.form.get("companyname").lower(),
            "companywebsite": request.form.get("companywebsite").lower(),
            "companynumber": request.form.get("companynumber"),
            "companylocation": request.form.get("companylocation"),
            "email": request.form.get("email"),
            "companyinfo": request.form.get("companyinfo")
        }
        mongo.db.providers.insert_one(register)

    return render_template('registercompany.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["username"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for("get_posts", username=session["username"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("login"))


@app.route("/createpost", methods=["GET", "POST"])
def createpost():
    if request.method == "POST":
        post = {
            "category_name": request.form.get("category_name"),
            "post_name": request.form.get("post_name"),
            "the_post": request.form.get("the_post"),
            "created_by": session["username"]
        }
        mongo.db.posts.insert_one(post)
        flash("Post Successfully Added")
        return redirect(url_for("get_posts"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("createpost.html", categories=categories)


@app.route("/editpost/<post_id>", methods=["GET", "POST"])
def editpost(post_id):
    creator = mongo.db.posts.find_one({"_id": ObjectId(post_id)}, {"created_by": 1})
    if session["username"] ==  creator["created_by"]:
        if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name"),
                "post_name": request.form.get("post_name"),
                "the_post": request.form.get("the_post"),
                "created_by": session["username"]
            }
            print(submit)
            mongo.db.posts.update({"_id": ObjectId(post_id)}, submit)
            flash("Post Successfully Updated")
            return redirect(url_for("get_posts"))

        posts = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("editpost.html", posts=posts, categories=categories)

    else:
        flash("You are not the creator of this post. You cannot edit it.")
        return redirect(url_for("get_posts"))


@app.route("/post/<post_id>")
def deletepost(post_id):
    creator = mongo.db.posts.find_one({"_id": ObjectId(post_id)}, {"created_by": 1})
    if session["username"] ==  creator["created_by"]:
        mongo.db.posts.remove({"_id": ObjectId(post_id)})
        flash("Post Successfully Deleted")
        return redirect(url_for("get_posts"))
    else:
        flash("You are not the creator of this post. You cannot edit it.")
        return redirect(url_for("get_posts"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


if __name__ == "__main__":
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        port=os.environ.get('PORT', '5000'),
        debug=False
    )
