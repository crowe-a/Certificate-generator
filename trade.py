import pandas as pd
import time
def trade():
    all_traded=[]
    traded=["",""]
    
    df = pd.read_excel('C:/Users/darkr/Desktop/creatcertifaket/Sertifika.xlsx')
    name=list(df["İsim"])
    email=list(df["E-Mail"])
    
    for(a,b) in zip(name,email):
       # a=unidecode(a)
        traded[0]=a
        traded[1]=b
        all_traded.append([a,b])
        #time.sleep(1)
        # print("name: ",a)
        # print("email: ",b)
        # print(name,email)
        # print(a,b)
        
        # coupons(a,"darkrenevatio@hotmail.com","C:/Users/darkr/Desktop/all/cradeandsendcertfikate/newcreater/sertifika.png","fontt/Poppins-Bold.ttf")
        # time.sleep(0.5)
    return all_traded

