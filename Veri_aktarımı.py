import snap7.client
from snap7.util import *
import snap7.util
import time

plc= snap7.client.Client()
plc.connect('192.168.1.5', 0, 1)


# Veri okuma işlemi
while True:

    int_data = plc.read_area(snap7.type.Areas.DB, 1, 0, 2)
    bool_data = plc.read_area(snap7.type.Areas.DB, 1, 2, 2)
    word_data = plc.read_area(snap7.type.Areas.DB, 1, 4, 2)
    bool5 = plc.read_area(snap7.type.Areas.DB, 1, 6, 2)
    erenreal = plc.read_area(snap7.type.Areas.DB, 1, 8, 4)

    print('Okunan int:', snap7.util.get_int(int_data, 0))
    print('Okunan bool:', snap7.util.get_bool(bool_data, 0, 0))
    print('Okunan word:', snap7.util.get_word(word_data, 0))
    print('Okunan bool5:', snap7.util.get_bool(bool5, 0, 0))
    print('Okunan erenreal:', snap7.util.get_real(erenreal, 0))

    print("-----------------------------------------")

    time.sleep(3)

