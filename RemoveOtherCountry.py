import os
import csv
import re
import datetime
import pandas as pd
from tqdm import tqdm

def RemoveOtherCountry(target_dir,output_dir):
    target_list = os.listdir(target_dir)
    if '.DS_Store' in target_list:                              #remove .DS_Store file
        target_list.remove('.DS_Store')
    for elem in tqdm(target_list):
        if '.csv' in elem:                                      #select only csv file
            row_date = re.search('\d{2}-\d{2}-\d{4}', elem)     #extract date
            file_date = pd.to_datetime(row_date.group())
            if file_date > datetime.date(2020,3,21):            #select only date after 03/21/2020
                complete_path = os.path.join(target_dir,elem)
                output_path = os.path.join(output_dir,elem)
                write_out = []
                with open(complete_path,'r',encoding='utf-8') as csvf:
                    csv_reader = csv.reader(csvf)
                    for line in csv_reader:
                        if line[0] == 'FIPS':                   #record the header
                            write_out.append(line)
                        else:
                            if line[3] == 'US':                 #record US country data
                                line[0] = str(line[0])
                                while len(line[0]) < 5:         #add zeros in front of FIPS
                                    line[0] = '0' + line[0]
                                write_out.append(line)
                with open(output_path,'w',encoding='utf-8') as f:
                    csv_writer = csv.writer(f)
                    for elem in write_out:
                        csv_writer.writerow(elem)




if __name__ == '__main__':
    print('program started')
    RemoveOtherCountry('COVID-19-datasets/csse_covid_19_data/csse_covid_19_daily_reports', 'COVID-19-US-county-level')
    print('program ended')




