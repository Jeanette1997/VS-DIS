import queryscript as qs
from faker import Faker
fake = Faker('da_DK')

# Brug denne til at oprette falske data
qlist=[]

for i in range(0, 10):
    qs.add_user(fake.name(), fake.email(), fake.phone_number())

qs.select_data('users', '*')