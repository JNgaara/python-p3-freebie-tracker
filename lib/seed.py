#!/usr/bin/env python3

# Script goes here!
from models import Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data
session.query(Company).delete()
session.query(Dev).delete()
session.query(Freebie).delete()

# Create companies
company1 = Company(name="Tech Corp", founding_year=2000)
company2 = Company(name="Code Masters", founding_year=2010)

# Create devs
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

# Add freebies
freebie1 = Freebie(item_name="Laptop", value=1000, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Mouse", value=50, dev=dev2, company=company2)

# Add to session and commit
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2])
session.commit()