import os
import csv
from tqdm import tqdm

def RemoveOtherCountry(target_dir,output_dir):
    target_list = os.listdir(target_dir)
    for elem in tqdm(target_list):
        if '.csv' in elem:                              #select only csv file
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




