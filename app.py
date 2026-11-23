from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
tasks = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if title:
            tasks.append(title)
        return redirect(url_for("home"))
    return render_template("index.html", tasks=tasks)

@app.route("/health")
def health():
    return jsonify(status="healthy", service="DevOps Task Tracker"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
