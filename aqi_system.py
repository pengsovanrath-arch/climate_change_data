environmental_data = {
  'sensor_id' = "PK_Lahore_East_05",
  'pm25_concentration' = 67.3,
  'carbon_monoxide_ppm' = 8,
  'humidity' = 68,
}

sensor_id = environmental_data['sensor_id']
pm25 = environmental_data['pm25_concentration']
co_ppm = environmental_data['carbon_monoxide_ppm']
humidity = environmental_data['humidity']

if pm25 >= 250 or co_ppm >= 100 or (humidity >= 80 and pm25 >= 150):
  status = "Hazardous"
  outdoor_activities = False
elif pm25 >= 55 or co_ppm >= 35 or (humidity >= 60 and pm25 >= 35):
  status = "Unhealthy"
  outdoor_activities = False
else:
  status = "Healthy"
  outdoor_activities = True


print(f"Country's Sensor ID: {sensor_id}")
print(f"PM Concentration: {pm25}")
print(f"Carbon Monoxide PPM: {co_ppm}")
print(f"Humidity Rate (%): {humidity}")
print(f"Status: {status}")
print(f"Outdoor Activities: {outdoor_activities}")
