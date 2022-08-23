#Schema structure

from app import d

class NessCapsules(d.Model):
    __tablename__ = 'capsules'
    capsule_id = d.Column(d.Integer,nullable=False,primary_key=True)
    capsule_name = d.Column(d.String(100),nullable=False)
    price = d.Column(d.Float,nullable=False)
    quantity = d.Column(d.Integer,nullable=True)
    customers = d.relationship('CustomerAccounts', backref='capsules')
    

class CustomerAccounts(d.Model):
    __tablename__ = 'customers'
    customer_id = d.Column(d.Integer,nullable=False,primary_key=True)
    customer_name = d.Column(d.String(100),nullable=False)
    paymethod = d.Column(d.String(100),nullable=False)
    capsule_id = d.Column(d.Integer,d.ForeignKey('capsules.capsule_id'),nullable=False)