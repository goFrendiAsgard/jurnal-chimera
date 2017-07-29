import sys, re, json
import matplotlib.pyplot as plt

def get_nano(chunk, pattern):
    for row in chunk:
        (str_part, num_part) = row.split(' : ')
        if(re.match(pattern, str_part)):
            return int(num_part.replace(',', ''))
    return 0

# get variable
config_file = sys.argv[1]
report_file = sys.argv[2]
config = json.loads(open(config_file, 'r').read())
report = open(report_file, 'r').read().split('\n')
process_count = len(config)
process_row_count = 4
session_row_count = process_row_count * process_count 
session_count = len(report) / session_row_count


# get data
data = []
for session_index in range(session_count):
    start = session_index * session_row_count
    end = (session_index + 1) * session_row_count
    chunk = report[start : end] 
    data_row = {} 
    for process_name in config:
        data_row[process_name] = {
                'start' : get_nano(chunk, r'\[INFO\] START PROCESS( +)\['+config[process_name]+'\]'),
                'end' : get_nano(chunk, r'\[INFO\] END PROCESS( +)\['+config[process_name]+'\]')
                }
    data .append(data_row)


# create plot
fig = plt.figure()
ax = fig.add_subplot(111)
nums = []
labels = []
csv_content = []
for session_index, session in enumerate(data):
    process_list = [session[process_name] for process_name in session]
    first = min([x['start'] for x in process_list])
    for process_index, process_name in enumerate(sorted(config.keys())):
        start = (session[process_name]['start'] - first) / 1000000000.0
        end = (session[process_name]['end'] - first) / 1000000000.0
        # bar
        bar_altitude = process_index + session_index * (process_count + 1)
        bar_width = end - start
        bar_left = start
        ax.barh(bar_altitude, bar_width, left=bar_left, height=0.8)
        # y-ticks
        nums.append(bar_altitude + 0.5)
        labels.append(process_name + ' #' + str(session_index + 1))
        # csv
        csv_row = ','.join([process_name, str(start), str(end)])
        csv_content.append(csv_row)

csv_content = '\n'.join(csv_content)
csv_file = report_file+'.csv'
csv_file_handle = open(csv_file,'w')
csv_file_handle.write(csv_content)
csv_file_handle.close()

plt.yticks(nums, labels)
plt.title('Chimera Framework Benchmark')

plt.show()
