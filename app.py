from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle

#Loading the model

model = open('cat_model.pkl','rb')
model_pred = pickle.load(model)

############################################################# Flask Calling ###########################################################  

app = Flask(__name__)
@app.route('/')
@cross_origin()
def home():
   return render_template("Used_Car_Price_Prediction.html")

@app.route("/predict", methods=["GET","POST"])
@cross_origin()
def predict():
	name = 0

	if request.method == 'POST':

		make_name =request.form['make']
		if make_name == 'Jeep':
			name =21
		elif make_name == 'Land Rover':
   			name =23
		elif make_name == 'Mazda':
			name =29
		elif make_name == 'Hyundai':
			name =18
		elif make_name == 'Chevrolet':
			name =8
		elif make_name == 'Lexus':
   			name =24
		elif make_name == 'Cadillac':
			name =7
		elif make_name == 'Chrysler':
			name =9
		elif make_name == 'Dodge':
			name =10
		elif make_name == 'Mercedes-Benz':
   			name =30
		elif make_name == 'Nissan':
			name =33
		elif make_name == 'Honda':
			name =16
		elif make_name == 'Kia':
			name =22
		elif make_name == 'Ford':
   			name =13
		elif make_name == 'Subaru':
			name =42
		elif make_name == 'BMW':
			name =4
		elif make_name == 'Audi':
			name =3
		elif make_name == 'Volkswagen':
   			name =45
		elif make_name == 'Jaguar':
			name =20
		elif make_name == 'Porsche':
			name =36
		elif make_name == 'GMC':
			name =14
		elif make_name == 'Toyota':
   			name =44
		elif make_name == 'Acura':
			name =0
		elif make_name == 'INFINITI':
			name =19
		elif make_name == 'Lincoln':
			name =25
		elif make_name == 'RAM':
   			name =37
		elif make_name == 'Volvo':
			name =46
		elif make_name == 'Mitsubishi':
			name =32
		elif make_name == 'Buick':
			name =6
		elif make_name == 'Mercury':
			name =31
		elif make_name == 'Scion':
   			name =41
		elif make_name == 'Saab':
			name =39
		elif make_name == 'Maserati':
			name =27
		elif make_name == 'Mini':
			name =26
		elif make_name == 'Genesis':
			name =15
		elif make_name == 'Saturn':
   			name =40
		elif make_name == 'FIAT':
			name =11
		elif make_name == 'Suzuki':
			name =43
		elif make_name == 'Fisker':
			name =12
		elif make_name == 'Pontiac':
			name =35
		elif make_name == 'Alfa Romeo':
			name =1
		elif make_name == 'Bentley':
			name =5
		elif make_name == 'Hummer':
   			name =17
		elif make_name == 'Maybach':
			name =28
		elif make_name == 'Aston Martin':
			name =2
		elif make_name == 'Oldsmobile':
   			name =34
		elif make_name == 'Rolls-Royce':
			name =38


		year = request.form['year']
		mileage = request.form['mileage']
		horsepower = request.form['horsepower']
		wheelbase = request.form['wheelbase']

		transmission_type = request.form['transmission']
		if transmission_type == 'Automatic':
			transmission =0
		elif transmission_type =='CVT':
			transmission =1
		elif transmission_type =='Dual Clutch':
			transmission =2
		else:
	 		transmission =3

		

		Price = model_pred.predict([[horsepower, mileage, year, name, wheelbase, transmission]])
		

		pred_price=round(Price[0],2)

		return render_template('Used_Car_Price_Prediction.html', prediction ="&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;&emsp; &emsp; &emsp; The Predicted Price of your Vehicle is $<i>{}</I>. <br><br> &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; This price is subject to fluctuate based on the vehicle's condition. </br></br> <table class=\"cart\" align=\"right\"> <td> <table class=\"result\" > <tr> <td> Make  </td> <td> {} </td> </tr> <tr> <td>Transmission  </td> <td> {} </td>  </tr><tr> <td>Horse Power  </td><td> {} (bhp) </td> </tr><tr> <td>Mileage  </td><td>{} (kmpl) </td> <tr/<tr><td>Wheel Base  </td><td>{} (inch) </td> <tr/> <tr> <td> Year  </td> <td>{} </td> </tr> </table> </td>  <td>  <div class=\"car\"></div> </td></table>".format(pred_price, make_name, transmission_type, horsepower, mileage, wheelbase, year))

	return render_template("Used_Car_Price_Prediction.html")


if __name__ == '__main__':
   app.run(debug=True)
