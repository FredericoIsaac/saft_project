from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import csv

# ------------------------------------- CONNECT APP TO POSTGRESQL ----------------------------------- #
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/senhas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ------------------------------------- CREATE TABLES ----------------------------------- #
class Companies(db.Model):
    client_id = db.Column(db.Integer, primary_key=True)
    financas = db.relationship('Financas', backref='companies', lazy=True)
    company = db.Column(db.String())
    nif = db.Column(db.Integer, unique=True)
    niss = db.Column(db.BigInteger, unique=True)

    def __repr__(self):
        return f'<Companies {self.client_id} {self.company}'


class Financas(db.Model):
    client_id = db.Column(db.Integer, db.ForeignKey('companies.client_id'), primary_key=True)
    password = db.Column(db.String())

    def __repr__(self):
        return f'<Finanças {self.client_id} {self.password}'


class SegSocial(db.Model):
    client_id = db.Column(db.Integer, db.ForeignKey('companies.client_id'), primary_key=True)
    password = db.Column(db.String())

    def __repr__(self):
        return f'<Segurança Social {self.client_id} {self.password}'


db.create_all()

# ------------------------------------- INSERT DATA TO DATABASE ----------------------------------- #

with open('senhas_db.csv', newline='') as file:
    reader = csv.reader(file, delimiter=';')
    count = 0
    for row in reader:
        if count == 0 or row[0] in ['10183', '10206']:
            count += 1
            continue

        client_id = int(row[0])
        company = row[1]
        nif = int(row[2])
        niss = int(row[3])
        pass_ss = row[4]
        pass_at = row[5]

        company = Companies(client_id=client_id, company=company, nif=nif, niss=niss)
        at = Financas(client_id=client_id, password=pass_at)
        seg_social = SegSocial(client_id=client_id, password=pass_ss)

        db.session.add_all([company, at, seg_social])
        db.session.commit()



