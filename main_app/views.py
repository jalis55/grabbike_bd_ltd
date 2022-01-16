
from main_app import app,mail,db
from flask import request,render_template,redirect,url_for,flash,session,jsonify
from main_app.forms import UserForm
from main_app.models import User
from random import *
from flask_mail import *

login_status=False

otp=randint(000000,999999)


@app.route('/',methods=['GET','POST'])
def home():
    # if session['logged_in']:
    #     return redirect(url_for('user_dashboard'))
    form=UserForm()
    # if request.method=='POST':
    #     if form.validate_on_submit():

    #         return str(form.email.data)
    return render_template('auth_templates/login.html',form=form)

@app.route('/login-check',methods=['GET','POST'])
def login_check():
    form=UserForm()
    if request.method == 'POST':
        user=User.query.filter_by(email=form.email.data).first()

        if user:
            
            session['user_email']=user.email
            recipient=session['user_email']
            msg=Message()
            msg.body=str(otp)
            msg.recipients=[recipient]
            msg.sender='jalismahamud2055@gmail.com'
            msg.subject='otp code'
            mail.send(msg)
            return render_template('auth_templates/email_otp.html')

        else:
            flash("Email Not Found")
            return redirect(url_for('home'))
    return redirect(url_for('home'))

@app.route('/otp-check',methods=['GET','POST'])
def otp_check():
    if request.method=='POST':
        if otp==int(request.form['otp']):
            session['logged_in']=True
            # login_status=True
            return redirect(url_for('user_dashboard'))
        
        flash('OTP not match')
        return render_template('auth_templates/email_otp.html')
    
            


        
    

@app.route('/user-dashboard')
def user_dashboard():
    if session['logged_in']:
    # if login_status:
        email=session['user_email']
        user=User.query.filter_by(email=email).first()
        return render_template('dashboard_templates/super_admin_content.html',user=user)
    else:
        return redirect(url_for('home'))

@app.route('/admin-control')
def admin_control():
    if session['logged_in']:
    # if login_status:
        email=session['user_email']
        user=User.query.filter_by(email=email).first()
        admins=User.query.filter_by(user_type='admin').all()
        

        return render_template('dashboard_templates/admin_control.html',user=user,admins=admins)
    else:
        return redirect(url_for('home'))

@app.route('/create-admin',methods=['POST'])
def create_admin():
    user=User(name=request.form['name'],email=request.form['email'],user_type='admin',approve_status=True)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('admin_control'))


@app.route('/sub-admin-control')
def sub_admin_control():

    if session['logged_in']:
    # if login_status:

        email=session['user_email']
        user=User.query.filter_by(email=email).first()
        sub_admins=User.query.filter_by(user_type='sub_admin').all()
        return render_template('dashboard_templates/sub_admin_control.html',user=user,admins=sub_admins)
    else:
        return redirect(url_for('home'))

@app.route('/create-subadmin')
def create_subadmin():
    if session['logged_in']:
    # if login_status:
        email=session['user_email']
        user=User.query.filter_by(email=email).first()
        sub_admins=User.query.filter_by(user_type='sub_admin').all()
        return render_template('dashboard_templates/subadmin.html',user=user,admins=sub_admins)
    else:
        return redirect(url_for('home'))
@app.route('/add-subadmin',methods=['POST','GET'])
def add_subadmin():
    if request.method=='POST':
        subadmin=User(name=request.form['name'],email=request.form['email'],user_type='sub_admin',approve_status=False)
        db.session.add(subadmin)
        db.session.commit()
        return redirect(url_for('create_subadmin'))
    
@app.route('/edit-subadmin/<int:id>')
def edit_subadmin(id):
    user=User.query.filter_by(id=id).first()
    if user.approve_status==False:
        user.approve_status=True
        db.session.commit()
    else:
        user.approve_status=False
        db.session.commit()
        

    return redirect(url_for('sub_admin_control'))
    
@app.route('/edit-user/<int:id>')
def edit_user (id):
    return str(id)

@app.route('/delete-user/<int:id>')
def delete_user(id):
    if session['logged_in']:
    # if login_status:
        user=User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('admin_control'))
    
@app.route('/delete-subadmin/<int:id>')
def delete_subadmin(id):
    if session['logged_in']:
    # if login_status:
        user=User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('sub_admin_control'))


      
        

@app.route('/logout')
def logout():
    session['logged_in']=False
    # login_status=False
    session['user_id']=''
    return redirect(url_for('home'))