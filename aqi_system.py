def environmental_sensor():
  
  environmental_data = [
    {'sensor_id': "PK_Lahore_East_05", 'pm25': 67.3, 'cm_ppm': 8, 'humidity': 68,},
    {'sensor_id': "KH_PhnomPenh_01", 'pm25': 33, 'cm_ppm': 0.5, 'humidity': 93,}
  ]

  result = []
  dangerous_zone = []

  environmental_data.sort(key=lambda sensor: sensor['pm25'])
  
  for sensor in environmental_data:
    sensor_id = sensor['sensor_id']
    pm25 = sensor['pm25']
    cm_ppm = sensor['cm_ppm']
    humidity = sensor['humidity']


  
    if pm25 >= 250 or cm_ppm >= 100 or (humidity >= 80 and pm25 >= 150):
      status = "Hazardous"
      outdoor_activities = False
      dangerous_zone.append({
        'sensor_id': sensor_id,
        'pm25': pm25,
        'cm_ppm': cm_ppm,
        'humidity': humidity,
        'status': status,
        'outdoor_activities': outdoor_activities
  
    })
    elif pm25 >= 55 or cm_ppm >= 35 or (humidity >= 60 and pm25 >= 35):
      status = "Unhealthy"
      outdoor_activities = False
    else:
      status = "Healthy"
      outdoor_activities = True


    result.append({
      'sensor_id': sensor_id,
      'pm25': pm25,
      'cm_ppm': cm_ppm,
      'humidity': humidity,
      'status': status,
      'outdoor_activities': outdoor_activities
  
    })

  return result, dangerous_zone

result, dangerous_zone = environmental_sensor()

for sensor in result:
  print(f"Country's Sensor ID: {sensor['sensor_id']}")
  print(f"PM Concentration: {sensor['pm25']}")
  print(f"Carbon Monoxide PPM: {sensor['cm_ppm']}")
  print(f"Humidity Rate (%): {sensor['humidity']}")
  print(f"Status: {sensor['status']}")
  print(f"Outdoor Activities: {sensor['outdoor_activities']}")
  print()

print(f"Country that is hazardous: ")

for info in dangerous_zone:
  
  print(f"Country's Sensor ID: {info['sensor_id']}")
  print(f"PM Concentration: {info['pm25']}")
  print(f"Carbon Monoxide PPM: {info['cm_ppm']}")
  print(f"Humidity Rate (%): {info['humidity']}")
  print(f"Status: {info['status']}")
  print(f"Outdoor Activities: {info['outdoor_activities']}")
  print()
