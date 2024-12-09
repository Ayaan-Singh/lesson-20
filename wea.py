weather = (1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1)
sunny = 0
rainy = 0
print (len(weather))
for i in range (0,18):
    if (weather[i] == 1):
     sunny += 1
    else :
       rainy +=1

print (sunny)
print(rainy)
if (sunny > rainy):
   print("good weather")
else:
   print ("bad weather")
