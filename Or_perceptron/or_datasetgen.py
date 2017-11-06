import csv

file1 = open('OR.txt','r') #open the and traing file
all_lines = csv.reader(file1,delimiter=' ') #read the file using csv reader

or_train_list = [] #to store the input list of and training data

or_percep_output = [] #to store the output of the perceptron of and training data

#iterate to store the data in the varialbles 
for row in all_lines :
   ls = [] 
   ls.append(float(1)) #x_0 = 0 by convention
   ls.append(float(row[0]))
   ls.append(float(row[1]))
   or_percep_output.append(float(row[2]))
   or_train_list.append(ls) 

#print the result to check o/p
#print and_train_list ;
#print and_percep_output ;
