def add_time(time,duration,day=None):
    wkd          = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    time_hr      = int(time.split(':')[0])
    time_min     = int(time.split(':')[1].split(' ')[0])
    time_am_or_pm     = time.split(":")[1].split(" ")[1]
    duration_hr  = int(duration.split(":")[0])
    duration_min = int(duration.split(':')[1])
    out_hr       = time_hr+duration_hr
    out_min      = time_min+duration_min
    out_am_or_pm = time_am_or_pm
    day          = ''
    if out_min >= 60:
        out_min -= 60
        out_hr  += 1
    if out_hr ==12:
        if out_am_or_pm=='AM':
            out_am_or_pm='PM'
        else:
            out_am_or_pm='AM'
    elif out_hr >12 and out_hr<24:
        if 12-time_hr<duration_hr and out_am_or_pm=='PM':
            day='(next day)'
        out_hr  -= 12
        if out_am_or_pm=='AM':
            out_am_or_pm='PM'
        else:
            out_am_or_pm='AM'
    elif out_hr >24:
        if out_am_or_pm=='PM':
            out_hr   += 12
            day = '('+str(int(out_hr/24))+' days later)'
            if out_hr%24==0:
                out_hr      = 12-(out_hr%24)
                out_am_or_pm='AM'
            else:
                out_hr = out_hr%24
                out_am_or_pm='AM'
        else:
            day = '('+str(int(out_hr/24))+' days later)'
            out_hr   = out_hr%24
    print(str(out_hr)+':'+str(out_min)+' '+out_am_or_pm+' '+day)
        
add_time("3:00 PM","3:10")
add_time("11:30 AM","2:32","Monday")
add_time("11:43 AM","00:20")
add_time("10:10 PM","3:30")
add_time("11:43 PM","24:20",'tueSday')
add_time("6:30 PM","205:12")