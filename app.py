from flask import Flask, render_template, request, redirect, url_for, flash,g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
app = Flask(__name__)
app.secret_key = "Secret Key"





app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_student_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
migrate = Migrate(app, db)



 
#Creating model table for our CRUD database
class students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key = True)
    citizenhip = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    education_departmant = db.Column(db.String(100))
    education_date_entered = db.Column(db.String(100))
    education_date_graduated = db.Column(db.String(100  ))
    education_degree = db.Column(db.String(100))
    education_stream = db.Column(db.String(100))
    employement_organization_name = db.Column(db.String(100))
    employement_city = db.Column(db.String(100))
    employement_country = db.Column(db.String(100))
    employement_from_date = db.Column(db.String(100))
    employement_position = db.Column(db.String(100))
    employement_industry = db.Column(db.String(100)) 
    employement_sector  = db.Column(db.String(100))
 
    def __init__(self, id,citizenhip,gender, education_departmant,education_date_entered,
    education_date_graduated,education_degree,education_stream,employement_organization_name,employement_city,
    employement_country,employement_from_date,employement_position,employment_industry,employment_sector):
        self.citizenhip = citizenhip
        self.id = id
        self.gender = gender
        self.education_departmant = education_departmant
        self.education_date_entered  = education_date_entered
        self.education_date_graduated = education_date_graduated
        self.education_degree = education_degree
        self.education_stream = education_stream

        self.employement_organization_name = employement_organization_name
        self.employement_city = employement_city
        self.employement_country = employement_country
        self.employement_from_date = employement_from_date
        self.employement_position = employement_position
        self.employment_industry = employment_industry
        self.employment_sector = employment_sector
 
 
 
 
#This is the index route where we are going to
#query on all our employee data
@app.route('/')
def Index():
    all_data = students.query.all()
    return render_template("index.html", students = all_data)
 
 
 
#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        id = request.form['id']
        citizenhip = request.form['citizenship']
        gender = request.form['gender']
        education_departmant = request.form['education_departmant']
        education_date_graduated = request.form['education_date_graduated']
        education_date_entered = request.form['education_date_entered']
        education_degree = request.form['education_degree']
        education_stream = request.form['education_stream']
        employement_organization_name = request.form['employement_organization_name']
        employement_city = request.form['employment_city']
        employement_country = request.form['employement_country']
        employement_from_date = request.form['employement_from_date']
        employement_position = request.form['employment_position']
        employement_industry = request.form['employment_industry']
        employement_sector = request.form['employment_sector']

        

 
 
        my_data = students(id,citizenhip,gender,education_departmant, education_date_entered,education_date_graduated,education_degree,education_stream,
        employement_organization_name,employement_city,employement_country,
        employement_from_date,employement_position,employement_industry,employement_sector)


        db.session.add(my_data)
        db.session.commit()
 
        flash("Employee Inserted Successfully")
 
        return redirect(url_for('Index'))
 
 
#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
 
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
 
        db.session.commit()
        flash("Employee Updated Successfully")
 
        return redirect(url_for('Index'))
 
 
 
 
#This route is for deleting our employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
 
    return redirect(url_for('Index'))
 
 
 
 
 
 
if __name__ == "__main__":
    app.run(debug=True)
