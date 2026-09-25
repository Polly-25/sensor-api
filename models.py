import faker
from faker import Faker
import random
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)


class Indicators(db.Model):
    __tablename__ = 'indicators'
    id = Column(Integer, nullable=False, primary_key=True, index=True)
    date_time = Column(DateTime, index=True)
    sensor_id = Column(Integer, ForeignKey('sensors.sensor_id'), index=True)
    value = Column(Integer)
class Sensor(db.Model):
    __tablename__ = 'sensors'
    sensor_id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
with app.app_context():
    db.create_all()

''' fake = Faker()
    for i in range(100):
            db.session.add(Sensor(name=f'sensor{i}'))
    db.session.commit()
    sensor_ids = [s.sensor_id for s in Sensor.query.all()]
    for i in range(1000000):
        date_time = fake.date_between(start_date=datetime(2020, 1, 1), end_date=datetime(2026, 5, 25))
        value = random.randint(0, 100)
        sensor_id = random.choice(sensor_ids)
        db.session.add(Indicators(date_time=date_time, value=value, sensor_id=sensor_id))
    db.session.commit()'''