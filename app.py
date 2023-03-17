from flask import Flask, jsonify, request, render_template
from process1 import *
from process2 import *
from datetime import datetime

def get_AQI_bucket(x):
    if x <= 50:
        return "Good"
    elif x <= 100:
        return "Satisfactory"
    elif x <= 200:
        return "Moderate"
    elif x <= 300:
        return "Poor"
    elif x <= 400:
        return "Very Poor"
    else:
        return "Severe"
    
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('Home.html')

@app.route("/aqi", methods=['GET', 'POST'])
def aqi_month():
	for key, value in request.form.items():
		if key == 'method2': 
			method2 = value
	dat=request.form['date']
	if method2 == 'Adilabad':
		result = adila(dat)
	elif method2 == 'karimnagar':
		result = karim(dat)
	elif method2 == 'khammam':
		result = kham(dat)
	elif method2 == 'Nizamabad':
		result = nizam(dat)
	else:
		result = waran(dat)   
    
	op =get_AQI_bucket(result)
	return render_template('result2.html',result=result,op=op)


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
			op='Be careful. There is chance of occuring heatwaves in adilabad in',month,'2023'
		else:
			op="you will be safe, there will be no chance of occuring heawaves in adilabad in",month," 2023"
	else:
		if result>=40:
			op="Be careful. There is chance of occuring heatwaves in" ,method, "in",month," 2023"
		elif result>=35 and result<=40:
			op="there may be chance of occuring the heatwave in" ,method, "in",month," 2023"
		else:
			op="you will be safe, there will be no chance of occuring heatwaves in ",method, "in",month,"2023"			
	return render_template('result1.html',result=result , op=op)

@app.route("/Project.html")
def project():
	return render_template('Project.html')
@app.route("/about.html")
def about():
    return render_template('about.html')
@app.route("/Home.html")
def Home():
	return render_template('Home.html')
if __name__=="__main__":
	app.run(debug=True)
