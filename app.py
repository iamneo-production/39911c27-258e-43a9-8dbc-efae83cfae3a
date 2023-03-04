from flask import Flask, jsonify, request, render_template
from process1 import *
from process2 import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=['GET', 'POST'])
def heatwave_month():
	for key, value in request.form.items():
		if key == 'method': 
			method = value
		if key == 'month': 
			month = value	
	
	if method == 'Adilabad':
		result = adilabad(month)
	elif method == 'karimnagar':
		result = karimnagar(month)
	elif method == 'khammam':
		result = khammam(month)
	elif method == 'Nizamabad':
		result = Nizamabad(month)
	else:
		result = warangal(month)
	if method=='Adilabad':
		if result>=35:
			op="Be careful. There is chance of occuring heatwaves in adilabad in ",month," 2023"
		else:
			op="you will be safe, there will be no chance of occuring heawaves"
	esle:
		if y>=40:
			op="Be careful. There is chance of occuring heatwaves in Kaimnagar in ",month," 2023"
		elif:
			op="there may be chance of occuring the heatwaves
		else:
			op="you will be safe, there will be no chance of occuring heawaves"
	return render_template('result.html',result=result)

if __name__=="__main__":
	app.run(debug=True)
