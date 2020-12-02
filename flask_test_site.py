from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# The site home page
@app.route("/<name>")  # this sets the route to this page
def home(name):
  return render_template("index.html", content=["dog", "rabbit", "bird", "squirrel"])

# Tests
  # return render_template("index.html", content=name, nbr=7)

# @app.route("/")  # this sets the route to the page
# def home():
# return "This is a test page <h1>HELLO</h1>"  

# @app.route("/<name>")
# def user(name):
#   return f"Hello {name}!!"

# @app.route("/admin/")
# def admin():
#   return redirect(url_for("user", name="Scott🏄"))
  
if __name__ == "__main__":
    app.run()

