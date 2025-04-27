import csv
import os

import random

class CSVHandler:

    def __init__(self, filename, separator=','):
        self.filename = filename
        self.separator =separator

        self.data =[]
        self.header = []
        self._load()


    def _load(self):
        with open(self.filename, newline ='', encoding  ='utf-8') as f:

            reader= csv.reader(f, delimiter=self.separator)
            self.header =next(reader)

            self.data =[row  for row in reader]

    def Show(self,mode ='top', count=5):

        total_rows = len(self.data)

        if total_rows == 0:
            print("The file is empty")


            return

        if total_rows< count:
            print(f"Only {total_rows} rows available not enough for {count}. Showing all rows:")

        selected_data = []
        if mode =='top':
            selected_data = self.data[:count]

        elif mode== 'bottom':
            selected_data = self.data[-count:]

        elif mode == 'random':
            selected_data = random.sample(self.data, min(count, total_rows))

        else:

            print(f"Unknown display mode: {mode}. Using 'top' by default.")
            selected_data = self.data[:count]


        print('\t'.join(self.header))

        for row in selected_data:

            print('\t'.join(row))

    def Info(self):

        num_rows = len(self.data)

        num_cols = len(self.header)
        print(f"{num_rows}x{num_cols}")

        for col_index, col_name in enumerate(self.header):
            non_empty = 0

            types_detected = set()

            for row in self.data:
                if col_index < len(row) and row[col_index].strip() != '':

                    non_empty += 1

                    value = row[col_index]
                    if value.isdigit():
                        types_detected.add('int')
                    else:

                        try:

                            float(value)
                            types_detected.add('float')

                        except ValueError:

                            types_detected.add('string')

            if 'string' in types_detected:

                final_type = 'string'
            elif 'float'in types_detected:

                final_type= 'float'
            elif 'int' in types_detected:

                final_type= 'int'

            else:
                final_type ='unknown'

            print(f"{col_name}\t{non_empty}\t{final_type}")

    def DelNaN(self):

        initial_count  = len(self.data)
        self.data= [row for row in self.data if all(cell.strip() !='' for cell in row)]

        removed =initial_count-len(self.data)
        print(f"Removed {removed} rows with empty fields")

    def MakeDS(self):

        if not self.data:

            print("No data available to split.")
            return

        random.shuffle(self.data)

        split_point = int(len(self.data) *0.7)
        train_data = self.data[:split_point]

        test_data = self.data[split_point:]


        if not os.path.exists('workdata'):
            os.makedirs('workdata/Learning')

            os.makedirs('workdata/Testing')

        with open('workdata/Learning/train.csv', 'w', newline= '', encoding  ='utf-8') as f_train:

            writer = csv.writer(f_train,delimiter =self.separator)
            writer.writerow(self.header)

            writer.writerows(train_data)

        with open('workdata/Testing/test.csv','w', newline  ='', encoding= 'utf-8') as f_test:
            writer = csv.writer(f_test, delimiter=self.separator)

            writer.writerow(self.header)
            writer.writerows(test_data)

        print("Data successfully spit and saved in 'workdata' folder")


handler = CSVHandler('sample.csv')
handler.Show()
handler.Info()

handler.DelNaN()
handler.MakeDS()
