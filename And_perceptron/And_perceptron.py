from and_datasetgen import and_train_list,and_percep_output

#method to calculate the dot prduct 
def calculateOutout (weights,parameters) :
     val = 0.0 
     i = 0 ;
     while(i<len(parameters)) :
        val+= weights[i]*parameters[i] 
        i+=1 
     return round(val,3) 
#__________________________end of method ___________________________________

 
#actuat program starts here :

w_i = [] # to store weights of and perceptron
prev_wi = [] # to store the weights of previous itration (used for iteration ))
it_count = 0  # to count number of itteration 
mu = 0.1 # learning rate of perceptron :



i = 0 ; #store an arbitrary values for weights
while(i < len(and_train_list[0])):
    w_i.append( round(0.2+ 0.2/(i+1),3) ) ;
    i+= 1 

print"\n------------------------------------------------------"
print "arbitrary weights are :"
print w_i,"\n"
print "learnig rate : ",mu ;
print "after every 10 iteration learning rate will be eaual to 0.5 times of original \n" 

#------------------------------------loop starts----------------------------------------
while(True) :
   it_count+= 1
   prev_wi = w_i 
   temp_wi = w_i
   w_i = []
   flag = True 
   i = 0 
   while(i < len(and_train_list)) :
        flag = True 
        op_i =  calculateOutout(prev_wi,and_train_list[i])
        # use perceptron rule o/p 
        if(op_i > 0) :
            oP_i = 1.0 
        else :
            op_i = -1.0  
        #perceptron rule o/p ends
        err_i = mu*(and_percep_output[i] - op_i) #percptron trining rule starts 
        j = 0 
        w_i = []
        while(j<len(prev_wi)) :
             w_i.append(round(prev_wi[j]+(err_i*and_train_list[i][j]),3))
             j+=1
        #end of percptron traing rule 
        prev_wi = w_i 
        i+=1
   i = 0 
   while(i<len(prev_wi)) :
      if(temp_wi[i] != w_i[i]) :
           flag = False
      i+=1
   if(it_count%10 == 0) :
       mu = mu/2.0 ;
   if(flag) :
        break ;
      

#--------------------------------------loop end --------------------------------------------


print"number of iteration  is : ",it_count
print"\nthe weights are : "
print w_i
print"------------------------------------------------------\n"

