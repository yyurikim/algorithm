def solution(today, terms, privacies):
    today = today.replace('.', '')
    term_info = {}
    for term in terms:
        code, month = term.split(' ')
        term_info[code] = int(month)
    
    date_amt = []
    result = []
    for i in range(len(privacies)):
        date, code = privacies[i].split(' ')
        year, month, day = map(int, date.split('.'))
        if day == 1:
            day = 28
            cal_month = month + term_info[code] - 1
        else:
            day -= 1
            cal_month = month + term_info[code]
        
        if cal_month > 12:
            month = cal_month % 12
            if month == 0:
                month = 12
                year = cal_month // 12 + year - 1
            else:
                year = cal_month // 12 + year
        else:
            month = cal_month
        
        
        due_date = int(str(year) + str(month).zfill(2) + str(day).zfill(2))
        
        
        if due_date - int(today) < 0:
            result.append(i+1)
            
    return result