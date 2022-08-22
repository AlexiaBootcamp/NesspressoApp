#Schema structure

from app import d

class NessCapsules(d.Model):
    capsule_id = d.Column(d.Integer,nullable=False,primary_key=True)
    capsule_name = d.Column(d.String(100),nullable=False)
    price = d.Column(d.float,nullable=False)
    quantity = d.Column(d.integer,nullable=True)
    

class CustomerAccounts(d.Model):
    customer_id = d.Column(d.Integer,nullable=False,primary_key=True)
    customer_name = d.Column(d.String(100),nullable=False)
    paymethod = d.Column(d.String(100),nullable=False)
    capsule_id = d.Column(d.Integer,d.ForeignKey('NessCapsules.capsule_id'),nullable=False)