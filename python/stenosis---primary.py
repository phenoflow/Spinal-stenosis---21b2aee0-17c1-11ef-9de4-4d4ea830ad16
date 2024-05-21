# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"N140.11","system":"readv2"},{"code":"N140z00","system":"readv2"},{"code":"43577.0","system":"readv2"},{"code":"97870.0","system":"readv2"},{"code":"41147.0","system":"readv2"},{"code":"3370.0","system":"readv2"},{"code":"106536.0","system":"readv2"},{"code":"93836.0","system":"readv2"},{"code":"15331.0","system":"readv2"},{"code":"93849.0","system":"readv2"},{"code":"98630.0","system":"readv2"},{"code":"91625.0","system":"readv2"},{"code":"94588.0","system":"readv2"},{"code":"73730.0","system":"readv2"},{"code":"12094.0","system":"readv2"},{"code":"35117.0","system":"readv2"},{"code":"72614.0","system":"readv2"},{"code":"69388.0","system":"readv2"},{"code":"9912.0","system":"readv2"},{"code":"52139.0","system":"readv2"},{"code":"62612.0","system":"readv2"},{"code":"45296.0","system":"readv2"},{"code":"M48.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('spinal-stenosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["stenosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["stenosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["stenosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
