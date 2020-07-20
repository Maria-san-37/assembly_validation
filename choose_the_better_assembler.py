#/usr/bin/env python
'''
María del Carmen Sánchez
Julio-2020
This program is for selecting the best assembler based on statistics of the assembly
'''
import re
import os
file = input("Enter the report file from Quast >>>")
os.system("sed 's/ /_/g' %r > salida1.txt" %file)
file1 = 'salida1.txt'
os.system("sed 's/^#_/num_/g' %r > salida2.txt" %file1)
file2 = 'salida2.txt'

def create_list(file2):
    metrics_dict = {}
    new_dict_min ={}
    new_dict_max = {}
    values_list = []
    keys_values= []
    pattern = re.compile('_{2,}')
    with open(file2, 'r') as f:
        with open('out.txt','w') as out:
            line = f.readline()
            for line in f:
                if line.strip():
                    line = re.sub(pattern,'\t',line)
                    line = line.split()
                    key = line[0]
                    value1 = line[1]
                    value2= line[2]
                    values = value1 +','+ value2
                    values = values.split(',')
                    metrics_dict[key]= values
                    assembler = metrics_dict.get('Assembly')
                    num_contigs = metrics_dict.get('num_contigs_(>=_0_bp)')
                    num_contigs_1000 = metrics_dict.get('num_contigs_(>=_1000_bp)')
                    num_contigs_5000 = metrics_dict.get('num_contigs_(>=_5000_bp)')
                    num_contigs_10000 = metrics_dict.get('num_contigs_(>=_10000_bp)')
                    num_contigs_25000 = metrics_dict.get('num_contigs_(>=_25000_bp)')
                    num_contigs_50000 = metrics_dict.get('num_contigs_(>=_50000_bp)')
                    total_length = metrics_dict.get('Total_length')
                    largest_contig = metrics_dict.get('Largest_contig')
                    N50 = metrics_dict.get('N50')
                    N75 = metrics_dict.get('N75')
                    L50 = metrics_dict.get('L50')
                    L75 = metrics_dict.get('L75')
                    num_misassemblies = metrics_dict.get('num_misassemblies')
                    Misassembled_contigs_length = metrics_dict.get('Misassembled_contigs_length')
                    num_local_misassemblies = metrics_dict.get('num_local_misassemblies')
                    num_indels_per_100_kbp = metrics_dict.get('num_indels_per_100_kbp')


    first_assembler = assembler[0]
    second_assembler = assembler[1]
    new_dict_min['total_num_contigs']  =  num_contigs
    new_dict_min['total_num_contigs>=1000bp'] = num_contigs_1000
    new_dict_min['total_num_contigs>=5000bp'] = num_contigs_5000
    new_dict_min['total_num_contigs>=10000bp'] = num_contigs_10000
    new_dict_min['total_num_contigs>=25000bp'] = num_contigs_25000
    new_dict_min['total_num_contigs>=50000bp'] = num_contigs_50000
    new_dict_max['total_length'] = total_length
    new_dict_max['largest_contig'] = largest_contig
    new_dict_max['N50'] = N50
    new_dict_max['N75'] = N75
    new_dict_min['L50'] = L50
    new_dict_min['L75'] = L75
    new_dict_min['num_misassemblies'] = num_misassemblies
    new_dict_min['misassembled_contigs_length']  = Misassembled_contigs_length
    new_dict_min['num_local_misassemblies'] = num_local_misassemblies
    new_dict_min['num_indels_per_100_kbp'] = num_indels_per_100_kbp

    count1 = 0
    count2 = 0
    for key, values in new_dict_min.items():
        if values[0] > values[1]:
            count1  += 1
        elif values[0] < values[1]:
            count2 += 1
        else:
            pass

    print('the %s type of assembly has %r good from 12' %(second_assembler,count1))
    print('the %s type of assembly has %r good from 12' %(first_assembler,count2))

    count3 = 0
    count4= 0
    for key, values in new_dict_max.items():
        if values[0] > values[1]:
            count3 += 1
        elif values[0] < values[1]:
            count4 += 1
        else:
            pass
    print('the assembler %s has %r good from 4' %(first_assembler,count3))
    print('the assembler %s has %r good from 4' %(second_assembler,count4))



create_list(file2)
