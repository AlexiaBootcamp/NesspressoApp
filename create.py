# Perform static database operations
from application import d
from application.schema import NessCapsules, CustomerAccounts

# Task -1 (only once)
d.create_all()
d.session.commit()

# Task - 2 (only once)
Ness1 = NessCapsules(capsule_id=1,capsule_name='Arondio',price=0.50,quantity=0.50)
d.session.add(Ness1)
Ness2 = NessCapsules(capsule_id=2,capsule_name='Stormio',price=0.65,quantity=150)
d.session.add(Ness2)
Ness3 = NessCapsules(capsule_id=3,capsule_name='Intenso',price=1.50,quantity=0.50)
d.session.add(Ness3)
Ness4 = NessCapsules(capsule_id=4,capsule_name='Scuro',price=2,quantity=180)
d.session.add(Ness4)

d.session.commit()

c1 = CustomerAccounts(customer_id=101,customer_name='Irini',paymethod='card',capsule_id=1)
d.session.add(c1)
c2 = CustomerAccounts(customer_id=102,customer_name='Alexia',paymethod='card',capsule_id=2)
d.session.add(c2)
c3 = CustomerAccounts(customer_id=103,customer_name='Dimitris',paymethod='card',capsule_id=4)
d.session.add(c3)
c4 = CustomerAccounts(customer_id=104,customer_name='Fotis',paymethod='card',capsule_id=1)
d.session.add(c4)

d.session.commit()

# Task - 3 (multiple times)
for ness in NessCapsules.query.all():
 print("- ",ness.capsule_name)
 for customeraccount in ness.customeraccounts:
  print("\t - ",customeraccount.customer_name)