import pandas as pd

class Bus:
     def __init__(self, namebusconductor, speedlimit, capacity, fare):
        self.namebusconductor = namebusconductor
        self.speedlimit = speedlimit
        self.capacity = capacity
        self.fare = fare

     def ShowVal(self):
        print("Name of bus conductor :",self.namebusconductor)
        print("Speedlimit of bus :",self.speedlimit,"Km/hr")
        print("Capacity of bus :",self.capacity)
        print("Fare of each person in bus :",self.fare,"rupees")
        print(" ")

     def BusBoard(self):
         df = pd.read_csv (r'C:\Users\prati\OneDrive\Documents\VS Code Projects\Cyborg OOPS Task\Station List.csv')
         
         list = df["Number of passengers waiting"].tolist()
         
         total = 0
         counter = 0
         cap = self.capacity

         while( counter < len(list) and total < cap):
            total = total + list[counter]
            counter += 1

         laststation = counter 
         diff = total - cap 

         listdup = list.copy()
         
         j = counter
         while (j < len(list)):            
            list[j] = 0 
            j += 1
         list[counter - 1] = list[counter - 1] - diff 

         rf = pd.DataFrame({"Number of passengers who are picked":list})

         i=0
         while (i < counter):            
            listdup[i] = 0 
            i += 1        
         listdup[counter - 1] = diff
         
         hf = pd.DataFrame({"Number of passengers who cannot be picked":listdup})

         df = pd.concat([df,rf,hf], axis=1)
         print(df) 
         print(" ")  
            
         dist = (laststation * 20) - 20         
         time = dist / self.speedlimit         
         print("The minimum duration for which the bus drives until the bus gets filled is", time,"hr")
         
         totalearn = self.capacity * self.fare

         print (" Bus Conductor Name :", self.namebusconductor)
         print (" His Total Earning is :", totalearn, "rupees")          
pass

Bus1 = Bus("Ranjit",40,25,20)

Bus.ShowVal(Bus1)

Bus.BusBoard(Bus1)

        
         

         
         
        

