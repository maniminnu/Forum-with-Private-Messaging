from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'random_secret_key'


messages = {}

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/message/<user>', methods=['GET', 'POST'])
def message(user):
    if request.method == 'POST':
        message_text = request.form['message']
        if user not in messages:
            messages[user] = []
        messages[user].append(message_text)
        return redirect(url_for('message', user=user))

    user_messages = messages.get(user, [])
    return render_template('message.html', user=user, user_messages=user_messages)

if __name__ == '__main__':
    app.run(debug=True)
