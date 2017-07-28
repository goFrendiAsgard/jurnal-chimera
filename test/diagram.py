import json
import matplotlib.pyplot as plt


def get_number(string):
    return  int(string.split(' : ')[1].replace(',', ''))

config = json.loads(open('config.json', 'r').read())
process_list = [x['name'] for x in config]

report = open('report.txt', 'r').read().split('\n')
data = []
for i in range(len(report)/(3*len(process_list))):
    data.append([])
    start = i*len(process_list)*3 # start index of each chunk
    first = min([get_number(x) for x in report[i*len(process_list)*3: (i+1)*len(process_list)*3 : 3]])
    #first = get_number(report[start])
    for j in range(len(process_list)):
        data[i].append({
            'start' : get_number(report[start+j*3]) - first,
            'end': get_number(report[start+j*3 + 1]) - first
            })
#print(data)

fig = plt.figure()
ax = fig.add_subplot(111)
nums = []
labels = []
for index_row, row in enumerate(data):
    for i in range(len(process_list)):
        print(row[i]['start'])
        ax.barh(i + index_row * (len(process_list)+1), row[i]['end'] - row[i]['start'], left=row[i]['start'], height=0.8)
        nums.append(i + index_row * (len(process_list)+1) + 0.5)
        labels.append(process_list[i] + ' #' + str(index_row+1))

plt.yticks(nums, labels)

plt.show()
