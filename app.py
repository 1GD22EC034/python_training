from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'raj_cse'
mysql = MySQL(app)


@app.route("/index",methods=["GET"])
def index():
    sql = "SELECT * FROM peoples"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    return render_template("index.html",results=results)


@app.route("/contact",methods=["GET"])
def contact():
    return render_template("contact.html")


@app.route("/blog",methods=["GET"])
def blog():
    return render_template("blog.html")



@app.route("/about",methods=["GET"])
def about():
    return render_template("about.html")


if __name__ == 'main':
    app.run()
