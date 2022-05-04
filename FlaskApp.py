from flask import Flask,render_template
from flask_bootstrap import Bootstrap
import json
# Press the green bu,tton in the gutter to run the script.

app = Flask(__name__)
Bootstrap(app)

@app.route("/status")
def status():

    with open("Status.json","r") as f:
        status = f.read()

    return render_template('index.html',
                           status=status)


@app.route("/create", methods=['GET'])
def create():

    with open("Status.json","w") as f:
        json.dump({"Status":"active"},f)

    return render_template('index.html',
                           status="created")


@app.route("/delete", methods=['GET'])
def delete():

    with open("Status.json","w") as f:
        json.dump({"Status":"Not Active"},f)

    return render_template('index.html',
                           status="deleted")


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)


