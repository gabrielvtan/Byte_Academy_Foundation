new_time = input("Time: ")
t=new_time.split(':')

total_minutes= int(t[0])*60+int(t[1])*1 +int(t[2])/60
print(total_minutes)