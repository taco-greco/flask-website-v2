from flask import Flask, render_template, jsonify 

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title' : 'Data Analyst',
    'location': 'Rouen, France',
    'salary': '30000€'
  },
   {
    'id': 2,
    'title' : 'Front-End Developer',
    'location': 'Athens, Greece',
    'salary': '18000€'
  },
  {
    'id': 3,
    'title' : 'Back-End Developer',
    'location': 'Remote',
    'salary': '28000€'
  }
]

@app.route("/")
def hello_tasos():
    return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__  == "__main__":
  app.run(host="0.0.0.0", debug=True)