# Perform static database operations

from schema import *

# Task -1 (only once)
# d.create_all()

# Task - 2 (only once)
# # c1 = NessCapsules(capsule_id=1,capsule_name='Oxford',price='UK',quantity='Oxana')
# d.session.add(c1)
# # c1 = NessCapsules(capsule_id=1,capsule_name='Oxford',price='UK',quantity='Oxana')
# d.session.add(c1)
# # c1 = NessCapsules(capsule_id=1,capsule_name='Oxford',price='UK',quantity='Oxana')
# d.session.add(c1)
# # c1 = NessCapsules(capsule_id=1,capsule_name='Oxford',price='UK',quantity='Oxana')
# d.session.add(c1)


# d.session.commit()

# p1 = Programs(program_id=1,program_name='M.S. Data Science',fees=5000,college_id=1)
# d.session.add(p1)



d.session.commit()

# Task - 3 (multiple times)
# for clg in Colleges.query.all():
#     print("- ",clg.college_name)
#     for program in clg.programs:
#         print("\t - ",program.program_name)