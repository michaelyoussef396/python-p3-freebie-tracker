#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Company, Dev, Freebie, Base

# Define a function to generate fake data


def generate_fake_data(session, num_companies=10, num_devs=20, num_freebies=50):
    fake = Faker()

    companies = []
    for _ in range(num_companies):
        company = Company(name=fake.company(), founding_year=fake.year())
        companies.append(company)

    devs = []
    for _ in range(num_devs):
        dev = Dev(name=fake.name())
        devs.append(dev)

    freebies = []
    for _ in range(num_freebies):
        freebie = Freebie(item_name=fake.word(), value=fake.random_int(min=1, max=1000),
                          dev=fake.random_element(devs), company=fake.random_element(companies))
        freebies.append(freebie)

    session.add_all(companies + devs + freebies)
    session.commit()


engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


generate_fake_data(session)


session.close()
