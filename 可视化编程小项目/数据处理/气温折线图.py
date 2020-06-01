import csv
import matplotlib.pyplot as plt
with open('weather.csv') as file:
    reader=csv.reader(file)
    # header_row=next(reader)
    # print(header_row)
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)
    a=[]
    for row in reader:
        for i in row:
            a.append(int(i))
    print(a)
    plt.plot(a,c='red')
    plt.xlabel('days',fontsize=16)
    plt.ylabel('temperatures',fontsize=16)
    plt.title('temperature of weather',fontsize=24)
    plt.tick_params(axis='both',which='major',labelsize=16)
    plt.show()