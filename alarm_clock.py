def alarm_clock(day, vacation):
  if day in range(1,6) and vacation == False:
      alarm =  "7:00"
      return alarm
  elif (day == 0 or day == 6) and vacation == False:
      alarm = "10:00"
      return alarm
  elif day in range(1,6) and vacation == True:
      alarm = "10:00"
      return alarm
  elif (day == 0 or day == 6) and vacation == True:
      alarm = "off"
      return alarm