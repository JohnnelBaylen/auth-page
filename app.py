from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, template_folder='auth', static_folder='styles')
app.secret_key = "yoursecretkey"

# Correct credentials stored in dictionary
ACCOUNT = {
    "Admin": "1234",
    "John": "john12",
    "User": "user12"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in ACCOUNT and ACCOUNT[username] == password:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return render_template("logIn.html", error="Invalid username or password")
    
    return render_template("logIn.html", error=None)

@app.route("/home")
def home():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("home.html", username=session["username"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
