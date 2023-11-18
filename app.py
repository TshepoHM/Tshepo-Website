from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    "id" : 1,
    "title" : "Python Developer",
    "location" : "Remote",
    "salary" : "R7 000"
  },
  {
    "id" : 2,
    "title" : "Java Developer",
    "location" : "Office",
    "salary" : "R8 000"
  }
]

@app.route("/")
def hello():
  return render_template("home.html", jobs = JOBS)
  




if __name__ == "__main__":
  app.run(host= "0.0.0.0", debug=True)
  
  