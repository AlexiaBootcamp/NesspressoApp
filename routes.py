#Routes and connectivity

from flask import render_template
from app import application
from schema import *

@application.route('/')
def root():
    return render_template('all_roots.html')

@application.route('/NessCapsules')
def capsule_list():
    all_NessCapsules = NessCapsules.query.all()
    return render_template('all_NessCapsules.html',list_of_capsules=all_NessCapsules)

@application.route('/NessCapsules/<int:id>')
def CustomerAccount(id):
    capsule_of_specific_customeraccount = CustomerAccounts.query.filter_by(capsule_id=id)
    NessCapsules = CustomerAccounts.query.get(id)
    return render_template('all_CustomerAccounts.html',list_of_customeraccount=capsule_of_specific_customeraccount,CustomerAccount=CustomerAccount)