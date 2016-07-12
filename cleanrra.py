#!/usr/bin/python
import sys, re

fp = '/var/www/cacti/rra/backups/azi_data_1755.rrd.xml'
f = open(fp)
ftext = f.read()

p = re.compile(ur'(lease\s([\d]*.*).*\n.*\n.*\n.*\n.*\n.*ethernet\s(.*);*.\n.*\n.*})')

raw_record = []

parsed_record = {}

for match in re.findall(p, ftext):
    raw_record.append(match)

for record in raw_record:
    m = re.search(p, record)
    parsed_record[m.group(2)] = m.group(3)

plaintext_record = []

for ip, mac in parsed_record.iteritems():
    plaintext_record.append("IP: {0}   MAC: {1}".format(ip, mac))
