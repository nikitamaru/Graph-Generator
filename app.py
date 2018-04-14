from flask import Flask, request, send_from_directory
from flask import  render_template as render
import graph, emails, os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
GRAPH_PATH = os.path.join(APP_ROOT, "files", "graphs")

@app.route('/')
def index():
    return render("index.html")

@app.route('/about')
def about():
    return render("about.html")

@app.route('/services')
def services():
    return render("services.html")

@app.route('/thanks', methods=["POST"])
def addMail():
    mailID = str(request.form["email"])
    emails.addMail(mailID)
    return render("thanks.html")

@app.route('/upload', methods=["POST"])
def upload():
    file = request.files['inputFile']
    graphTitle = request.form['title']
    xAxisLabel = request.form['xName']
    yAxisLabel = request.form['yName']
    filename = file.filename
    csvFile = os.path.join(APP_ROOT, "files", "csvs", filename)
    file.save(csvFile)
    graph.chartGen(csvFile, graphTitle, xAxisLabel, yAxisLabel)
    return send_from_directory(directory=GRAPH_PATH, filename="chart.pdf")

if __name__=='__main__':
    app.run(debug=True)
