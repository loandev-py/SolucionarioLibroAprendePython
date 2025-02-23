# *****************
# FICHO CUANDO TOCA
# *****************


def run(time: str, offset: int) -> str:
    
    hour, minute  =  map(int, time.split(':'))
    
    total_minutes = hour * 60 + minute + offset
    
    new_hours = (total_minutes // 60 ) % 24
    new_minutes = total_minutes % 60

    return f'{new_hours}:{new_minutes:02d}'

if __name__ == '__main__':
    run('17:15', 240)