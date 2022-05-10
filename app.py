from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import cgi, cgitb, jinja2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, flash, request, redirect, url_for


#Loading the model

model = open('cat_model.pkl','rb')
model_pred = pickle.load(model)


############################################################# Flask Calling ###########################################################  

app = Flask(__name__)
engine = create_engine('sqlite:///logindb.db', echo=True)
cgitb.enable()


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    print(request.form['email'])
    POST_USERNAME = str(request.form['email'])
    POST_PASSWORD = str(request.form['password'])
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.email.in_([POST_USERNAME]))
    result = query.first()
    if not result or not check_password_hash(result.password, POST_PASSWORD):
        flash('Please check your login details and try again.')
        return home()
    else:
        session['logged_in']=True
        return render_template("Used_Car_Price_Prediction.html")

@app.route('/signup', methods=['POST'])
def signin():
    USERNAME = str(request.form['uname'])
    PASSWORD = str(request.form['password'])
    EMAIL = str(request.form['email'])
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([USERNAME]), User.password.in_([PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
        return render_template("Used_Car_Price_Prediction.html")
    else:
        new_user = User(email=EMAIL, username=USERNAME, password=generate_password_hash(PASSWORD, method='sha256'))
        s.add(new_user)
        s.commit()
        return home()



@app.route("/predict", methods=["GET","POST"])
@cross_origin()
def predict():
	name = 0
	body = 0

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
		body_type = request.form['body']
		if body_type == 'SUV':
			body =5
		elif body_type =='Sedan':
			body =6
		elif body_type =='Coupe':
			body =1
		elif body_type =='Pickup Truck':
			body =4
		elif body_type =='Wagon':
			body =8
		elif body_type =='Minivan':
			body =3
		elif body_type =='Hatchback':
			body =2
		elif body_type =='Convertible':
			body =0
		else:
	 		body =7

		transmission_type = request.form['transmission']
		if transmission_type == 'Automatic':
			transmission =0
		elif transmission_type =='CVT':
			transmission =1
		elif transmission_type =='Dual Clutch':
			transmission =2
		else:
	 		transmission =3

		

		Price = model_pred.predict([[horsepower, mileage, year, name, body, transmission]])
		

		pred_price=round(Price[0],2)

		return render_template('Used_Car_Price_Prediction.html', prediction ="&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;&emsp; &emsp; &emsp; The Predicted Price of your Vehicle is $<i>{}</I>. <br><br> &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; This price is subject to fluctuate based on the vehicle's condition. </br></br> <table class=\"cart\" align=\"right\"> <td> <table class=\"result\" > <tr> <td> Make  </td> <td> {} </td> </tr> <tr> <td>Transmission  </td> <td> {} </td>  </tr><tr> <td>Horse Power  </td><td> {} (bhp) </td> </tr><tr> <td>Mileage  </td><td>{} (kmpl) </td> <tr/<tr><td>Body Type  </td><td>{} </td> <tr/> <tr> <td> Year  </td> <td>{} </td> </tr> </table> </td>  <td>  <div class=\"car\"></div> </td></table>".format(pred_price, make_name, transmission_type, horsepower, mileage, body_type, year))

	return render_template("Used_Car_Price_Prediction.html")


@app.route("/logout", methods=['POST'])
def logout():
    session['logged_in'] = False
    return home()



if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(ssl_context='adhoc',debug=True,host='172.31.17.213',port=8081)
