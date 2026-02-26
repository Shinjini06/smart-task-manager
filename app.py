from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        if os.stat(FILE_NAME).st_size == 0:
            return []
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


@app.route("/", methods=["GET", "POST"])
def index():
    tasks = load_tasks()

    if request.method == "POST":
        task_name = request.form["task"]
        priority = request.form["priority"]

        tasks.append({
            "task": task_name,
            "priority": priority,
            "completed": False
        })

        save_tasks(tasks)
        return redirect("/")

    return render_template("index.html", tasks=tasks)


@app.route("/complete/<int:task_id>")
def complete(task_id):
    tasks = load_tasks()
    tasks[task_id]["completed"] = True
    save_tasks(tasks)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
