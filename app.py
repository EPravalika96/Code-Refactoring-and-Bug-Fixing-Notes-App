from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)

# Configure the Flask-Session extension
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note is not None:
            if 'notes' not in session:
                session['notes'] = []
            session['notes'].append(note)

            # Redirect to a different route after handling the POST request
            return redirect(url_for('index'))

    return render_template("home.html", notes=session.get('notes', []))

@app.route('/clear_note/<int:index>', methods=["POST"])
def clear_note(index):
    if 'notes' in session and 0 <= index < len(session['notes']):
        del session['notes'][index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
