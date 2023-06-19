conference = [('знакомство', '10:00 - 11:00', 'Иван'), ('прощание', '11:00 - 12:00', 'Юрий')]
wait = False

def show_timeline(conference):
    count = 0
    while count < len(conference):
        for name, time, speaker in conference:
            count+=1
            return name, time, speaker


def find_perfomance(now_time):
    hour = now_time.split(':')
    if hour[0] in conference and wait == False:
        return 1