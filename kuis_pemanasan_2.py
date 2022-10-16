hour = int(input("Jam : "))
minute = int(input("Menit : "))
seconds = int(input("Detik : "))

SECOND_PER_HOUR = 3600

seconds_from_hour = hour * SECOND_PER_HOUR

SECOND_PER_MINUTES = 60

seconds_from_minutes = minute * SECOND_PER_MINUTES

total_seconds = seconds_from_hour + seconds_from_minutes + seconds

total_seconds_after_1_s = total_seconds + 1

hour_after_1_s = (total_seconds_after_1_s // SECOND_PER_HOUR) % 24

minute_after_1_s = (total_seconds_after_1_s % SECOND_PER_HOUR ) // SECOND_PER_MINUTES 

seconds_after_1_s = total_seconds_after_1_s % SECOND_PER_MINUTES

print("waktu satu detik kemudian adalah",hour_after_1_s,"-",minute_after_1_s,"-",seconds_after_1_s)

