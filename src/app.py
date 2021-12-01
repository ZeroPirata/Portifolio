from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def about_me():
    return render_template('sobremim.html')

@app.route("/escolaridade")
def school():
    return render_template('escolaridade.html')

@app.route("/projetos")
def project():
    return render_template('projetos.html')

@app.route("/curriculo")
def curriculo():
    return render_template('curriculo.html')

@app.route("/hobby")
def hobby():
    return render_template('hobby.html')

if __name__ == '__main__':
    app.run()