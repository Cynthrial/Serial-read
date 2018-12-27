#!/usr/bin/env python
# -*- coding: utf-8 -*

import serial
import serial.tools.list_ports

port_list = list(serial.tools.list_ports.comports())
mac_list = []
count = 0

if len(port_list) <= 0:
    print "The Serial port can't find!"

else:
    port_list_0 = list(port_list[0])

    port_serial = port_list_0[0]

    ser = serial.Serial(port_serial, 115200, timeout=520)

    print "Link...", ser.name
    data = ''
    while 1:
        while ser.inWaiting() > 0:
            data += ser.read(1)

        if data != '':
            mac_list.insert(count, data)
            mac_list = list(set(mac_list))
            count = len(mac_list)

            print "当前有" + str(count) + "个客户端在线，分别是"
            print mac_list
            print ""
            data = ''