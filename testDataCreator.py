from faker import Faker
fake = Faker('da_DK')

# Brug denne til at oprette falske data
qlist=[]


def fakeToSQL():
    """Generer SQL INSERT statements for testdata."""
    sql_statements = []
    for i in range(0, 10):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        password = fake.password()
        sql_statements.append(f"INSERT INTO users (name, email, phone_nr, password) VALUES ('{name}', '{email}', '{phone}', '{password}');")
    return sql_statements
