from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task", "").strip()
        if task:
            tasks.append(task)
        return redirect(url_for("home"))
    return render_template("index.html", tasks=tasks)

@app.route("/health")
def health():
    return jsonify({
        "service": "DevOps Task Tracker",
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
