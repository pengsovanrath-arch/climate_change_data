sensor_id = "PK_Lahore_East_05"
pm25_concentration = 67.3
carbon_monoxide_ppm = 8
humidity = 68


if pm25_concentration >= 250 or carbon_monoxide_ppm >= 100 or (humidity >= 80 and pm25_concentration >= 150):
  status = "Hazardous"
  outdoor_activities = False
elif pm25_concentration >= 55 or carbon_monoxide_ppm >= 35 or (humidity >= 60 and pm25_concentration >= 35):
  status = "Unhealthy"
  outdoor_activities = False
else:
  status = "Healthy"
  outdoor_activities = True


print(f"Country's Sensor ID: {sensor_id}")
print(f"PM Concentration: {pm25_concentration}")
print(f"Carbon Monoxide PPM: {carbon_monoxide_ppm}")
print(f"Humidity Rate (%): {humidity}")
print(f"Status: {status}")
print(f"Outdoor Activities: {outdoor_activities}")
