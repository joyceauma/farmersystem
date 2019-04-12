#Here we import the three models we need to import data into
from accounts.models import District, Subcounty, Parish


import csv

def uploadCSV():
	
	
    f = open("./district.csv")
	
	
    reader = csv.reader(f)
	
	
    for d,s,p in reader:
		
		
		
		
        district,created = District.objects.get_or_create(name=d)
		
		
        subcounty,created = Subcounty.objects.get_or_create(name=s, district=district)
    
        Parish.objects.create(name=p,sub_county=subcounty)
          
      
        print(f'added {d} , {s}, {p}')
    return "YEAH"


uploadCSV()