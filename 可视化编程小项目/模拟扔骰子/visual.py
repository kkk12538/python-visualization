

def Visual(new_die,times):
    new_die.rolling(times)
    sum_results=[]
    for i in range(1,new_die.die_num+1):
        sum_results.append(new_die.results.count(i))
    return sum_results
