#! /usr/bin/env python3

import sys
import csv
import json
import io
import sys

json_file_path = sys.argv[1].strip()

json_str = ''
with open(json_file_path) as f:
    json_str = ' '.join(f.readlines())

json_data = json.loads(json_str)
column_names = json_data[0].keys()

output = io.StringIO()
csv_writer = csv.writer(output)
csv_writer.writerow(column_names)

for obj in json_data:
    csv_writer.writerow(obj.values())

print(output.getvalue())
