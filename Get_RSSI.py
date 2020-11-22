import subprocess
from csv import writer
import datetime

start_time = datetime.datetime.now()
print("Start time: ", start_time.strftime("%Y-%m-%d , %H:%M:%S"))

while True:

    loop_start_time = datetime.datetime.now()


    def get_client_rssi():
        results = subprocess.check_output(["netsh", "wlan", "show", "interface"]).decode()

        lines = results.split('\r\n')

        d = {}
        for line in lines:
            if ':' in line:
                vals = line.split(': ')
                if vals[0].strip() != '' and vals[1].strip() != '':
                    d[vals[0].strip()] = vals[1].strip()

        for key in d.keys():
            if key == "Signal":
                return d[key]


    def get_bssid():
        results = subprocess.check_output(["netsh", "wlan", "show", "interface"]).decode()

        lines = results.split('\r\n')

        d = {}
        for line in lines:
            if ':' in line:
                vals = line.split(': ')
                if vals[0].strip() != '' and vals[1].strip() != '':
                    d[vals[0].strip()] = vals[1].strip()

        for key in d.keys():
            if key == "BSSID":
                return d[key]


    def get_channel():
        results = subprocess.check_output(["netsh", "wlan", "show", "interface"]).decode()

        lines = results.split('\r\n')

        d = {}
        for line in lines:
            if ':' in line:
                vals = line.split(': ')
                if vals[0].strip() != '' and vals[1].strip() != '':
                    d[vals[0].strip()] = vals[1].strip()

        for key in d.keys():
            if key == "Channel":
                return d[key]

    def append_list_as_row(file_name, list_of_elem):
        with open(file_name, 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(list_of_elem)

    client_rssi = get_client_rssi()
    bssid = get_bssid()
    channel = get_channel()
    now = datetime.datetime.now()
    time_now = now.strftime("%H:%M:%S")
    loop_end_time = datetime.datetime.now() - loop_start_time
    total_time_taken = datetime.datetime.now() - start_time

    output_list = (bssid, channel, client_rssi, time_now, loop_end_time, total_time_taken)

    append_list_as_row('output.csv', output_list)
