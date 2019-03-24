import pandas as pd
from DataExtractor import DataExtractor
from Utils import PathHelper
from random import randint
import socket

from multiprocessing.pool import ThreadPool


class NetworkExtractor(DataExtractor):

    def connect(self):
        pass

    def getAllIp(self, start_ip, stop_ip):
        ips = []
        tmp = []

        for i in start_ip.split('.'):
            tmp.append("%02X" % int(i))

        start_dec = int(''.join(tmp), 16)
        tmp = []

        for i in stop_ip.split('.'):
            tmp.append("%02X" % int(i))

        stop_dec = int(''.join(tmp), 16)

        while(start_dec < stop_dec + 1):
            bytes = []
            bytes.append(str(int(start_dec / 16777216)))
            rem = start_dec % 16777216
            bytes.append(str(int(rem / 65536)))
            rem = rem % 65536
            bytes.append(str(int(rem / 256)))
            rem = rem % 256
            bytes.append(str(rem))
            ips.append(".".join(bytes))
            start_dec += 1

        return ips

    def execute(self, action, start_ip=None, stop_ip=None):
        # pool = ThreadPool(processes=5)

        if action == 'DnsLookup':
            ips = self.getAllIp(start_ip, stop_ip)

            self.result = []
            while len(ips) > 0:
                i = randint(0, len(ips) - 1)
                lookup_ip = str(ips[i])

                try:
                    host = {}
                    host['ip'] = lookup_ip
                    # async_result = pool.apply_async(socket.gethostbyaddr(lookup_ip)[0])
                    # host['name'] = async_result.get()  
                    host['name'] = socket.gethostbyaddr(lookup_ip)[0]
                except (socket.herror, socket.error):
                    print('ERRORE *****************************************************')
                    pass

                print('***********************************************************')
                print(self.result)
                self.result.append(host)
                del ips[i]


    def toDataframe(self):
        self.df = pd.DataFrame(self.result)
        return self.df

    """
    def checkPorts(self, ip):
    # TODO Draft
        try:
            for port in range(1,1025):  
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print("Port {}: 	 Open".format(port))
                sock.close()

        except KeyboardInterrupt:
            print("You pressed Ctrl+C")
            sys.exit()

        except socket.gaierror:
            print('Hostname could not be resolved. Exiting')
            sys.exit()

        except socket.error:
            print("Couldn't connect to server")
            sys.exit()

        # Checking the time again
        t2 = datetime.now()

        # Calculates the difference of time, to see how long it took to run the script
        total =  t2 - t1

        # Printing the information to screen
        print('Scanning Completed in: ', total)
    """