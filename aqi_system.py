import numpy as np

def environmental_sensor():

  environmental_data = np.array([
    ['PK_Lahore_East_05', 67.3, 8, 68],
    ['KH_PhnomPenh_01', 33, 0.5, 93]
  ])


  environment_in_pk_lahore_east = environmental_data[0, :]
  environment_in_phnompenh = environmental_data[1, :]
  sensor_id = environmental_data[:, 0]
  pm25 = environmental_data[:, 1].astype(float)
  cm_ppm = environmental_data[:, 2].astype(float)
  humidity = environmental_data[:, 3].astype(float)


  for i in range(len(sensor_id)):
    
    if pm25[i] >= 250 or cm_ppm[i] >= 100 or (humidity[i] >= 80 and pm25[i] >= 150):
      status = "Hazardous"
      outdoor_activities = False
    elif pm25[i] >= 55 or cm_ppm[i] >= 35 or (humidity[i] >= 60 and pm25[i] >= 35):
      status = "Unhealthy"
      outdoor_activities = False
    else:
      status = "Healthy"
      outdoor_activities = True


    print(f"Sensor ID: {sensor_id[i]}")
    print(f"Status: {status}")
    print(f"Outdoor Activities: {outdoor_activities}")
    print()


environmental_sensor()

