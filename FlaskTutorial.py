from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated database
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append({"id": len(tasks), "name": task})
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = tasks[task_id]
    if request.method == 'POST':
        new_name = request.form.get('task')
        if new_name:
            task['name'] = new_name
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks.pop(task_id)
    # Reassign IDs
    for i, task in enumerate(tasks):
        task['id'] = i
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
