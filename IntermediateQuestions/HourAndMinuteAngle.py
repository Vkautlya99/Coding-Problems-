def HourAndMinuteAngle(hour, minute):
    hour_angle = 30 * hour + 0.5 * minute
    minute_angle = 6 * minute
    
    angle = abs(minute_angle - hour_angle)
    return min(angle, 360 -angle)

hour = 9
minute = 00
print(HourAndMinuteAngle(hour, minute))

