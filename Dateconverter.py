dates = ["2010/02/20", "19/12/2016", "11-18-2012", "20130720"]
#Checked if it is February, but did not check for years with 29 days.
def transformDateFormate(dates):
    new_dates = []
    for i in range(len(dates)):
        if(len(dates[i]) == 10 and (dates[i].count('-') == 2 or dates[i].count('/') == 2)):
            if('-' in dates[i]):
                strs = dates[i].split('-')
                if(int(strs[0]) <13 and int(strs[0]) > 0 and int(strs[2]) > 0 and int(strs[2]) < 2024 and len(strs[0]) == 2 and len(strs[1]) == 2 and len(strs[2]) == 4):
                    if((int(strs[0]) == 2 and int(strs[1]) > 0 and int(strs[1]) < 30) or (int(strs[1]) > 0 and int(strs[1]) < 32)):
                        new_dates.append(strs[2] + strs[0] + strs[1])
            else:            
                strs = dates[i].split('/')
                if(len(strs[0]) == 4):
                    if(int(strs[1]) <13 and int(strs[1]) > 0 and int(strs[0]) > 0 and int(strs[0]) < 2024 and len(strs[2]) == 2 and len(strs[1]) == 2 and len(strs[0]) == 4):
                        if((int(strs[1]) == 2 and int(strs[2]) > 0 and int(strs[2]) < 30) or (int(strs[2]) > 0 and int(strs[2]) < 32)):
                            new_dates.append(strs[0] + strs[1] + strs[2])
                else:
                    if(int(strs[1]) <13 and int(strs[1]) > 0 and int(strs[2]) > 0 and int(strs[2]) < 2024 and len(strs[2]) == 4 and len(strs[1]) == 2 and len(strs[0]) == 2):
                        if((int(strs[1]) == 2 and int(strs[0]) > 0 and int(strs[0]) < 30) or (int(strs[0]) > 0 and int(strs[0]) < 32)):
                            new_dates.append(strs[2] + strs[1] + strs[0])
    return new_dates
print(transformDateFormate(dates))