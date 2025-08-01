import fileinput
import datetime

if __name__ == "__main__":
    for line in fileinput.input('BuildTime.py', inplace=True):
        if 'self.build_time = ' in line:
            time_stamp = datetime.datetime.now().isoformat(timespec='seconds')
            time_stamp = time_stamp.replace('T', ' ')
            print('        self.build_time = "{}"\n'.format(time_stamp), end='')
        else:
            print(line, end='')