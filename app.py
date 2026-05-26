from flask import jsonify, request
from models import Indicators, Sensor, app, db
from datetime import datetime
from sqlalchemy import func


@app.route('/information/<int:sensor_id>', methods=['GET'])
def get_information(sensor_id):
    sensor = db.session.get(Sensor, sensor_id)
    start_date = datetime.strptime(request.args.get('start_date'), '%Y-%m-%d')
    end_date = datetime.strptime(request.args.get('end_date'), '%Y-%m-%d')
    if sensor is None:
        return jsonify({"error": "sensor not found"}, 404)
    if start_date < datetime(2020, 1, 1):
        return jsonify({"error": "Your date is less than required"}, 400)
    if end_date > datetime(2026, 5,25):
        return jsonify({"error": "Your date is longer than required "}, 400)
    result = db.session.query(
        func.avg(Indicators.value).label('avg_value'),
        func.count(Indicators.id).label('count')
    ).filter(
        Indicators.sensor_id == sensor_id,
        Indicators.date_time >= start_date,
        Indicators.date_time <= end_date
    ).one()
    return jsonify({
        "sensor_id": sensor_id,
        "start": request.args.get('start_date'),
        "end": request.args.get('end_date'),
        "avg_value": result.avg_value,
        "count": result.count
    })
if __name__=="__main__":
    app.run(debug=True, port=8080)
