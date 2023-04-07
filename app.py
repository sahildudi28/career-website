from flask import Flask, render_template, jsonify

app = Flask(__name__)
STAT = [{
  'id': 'batting',
  'style': 'right hand batsman'
}, {
  'id': 'bowling',
  'style': 'right arm medium'
}]


@app.route("/")
def hello():
  return render_template("home.html", stat=STAT, my_name='Sahil Dudi')


@app.route("/api/stat")
def stats():
  return jsonify(STAT)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
