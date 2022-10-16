def check_hour(hour):
    return 0 <= hour <= 23

def check_minutes(minutes):
    return 0 <= minutes <= 59

def check_seconds(seconds):
    return 0 <= seconds <= 59


def hour_to_seconds(hour):
    return hour * 3600

def minute_to_seconds(minutes):
    return minutes * 60

def after_seconds(total_seconds):
    return total_seconds+1

def new_hour(total_seconds):
    DETIK_PER_JAM = 3600
    new_hour =  (total_seconds // DETIK_PER_JAM ) % 24
    return new_hour

def new_minute(total_seconds):
    DETIK_PER_MENIT = 60
    DETIK_PER_JAM = 3600
    new_minute = (total_seconds % DETIK_PER_JAM ) // DETIK_PER_MENIT
    return new_minute

def new_seconds(total_seconds):
    DETIK_PER_MENIT = 60
    new_seconds = total_seconds & DETIK_PER_MENIT
    return new_seconds

if __name__ == '__main__':
    status = False
    while not status:
        jam = int(input("Input Jam   : "))
        menit = int(input("Input Menit : "))
        detik = int(input("Input Detik : "))
        if check_hour(jam) and check_minutes(menit) and check_seconds(detik):
            status = True
    
    total_seconds_before = hour_to_seconds(jam) + minute_to_seconds(menit) + detik
    total_seconds_after = after_seconds(total_seconds_before)

    print(f"Waktu satu detik ke depan : ({new_hour(total_seconds_after)},{new_minute(total_seconds_after)},{new_seconds(total_seconds_after)})")
    