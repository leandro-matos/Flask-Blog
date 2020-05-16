import db
from flask import Flask, abort, url_for

app = Flask(__name__)

@app.route('/')
def index():
    html = ['<ul>']
    for equipe, time in db.times.items():
        html.append(
            f"<li><a href='{url_for('time', equipe=equipe)} '>{time['name']}</a></li><br>"
        )
    html.append('</ul>')
    return '\n'.join(html)

def profile(equipe):
    time = db.times.get(equipe)

    if time:
        return f"""
            <h1>{time['name']}</h1>
            <img src="{time['image']}"/><br/>
            País: {time['pais']} <br/><br/>
            <a href="/">Voltar</a>
        """
    else:
        return abort(404, "Team not Found")

app.add_url_rule('/profile/<equipe>/', view_func=profile, endpoint='time')
app.run(use_reloader=True)

