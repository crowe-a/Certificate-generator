import trade,creatter,sender

font="C:/Users/darkr/Desktop/all/cradeandsendcertfikate/fontt/Poppins-Bold.ttf"
certifica="C:/Users/darkr/Desktop/creatcertifaket/sertifika.png"

for i in trade.trade():
    try:
        print(i)
        creatter.coupons(i[0],certifica,font)
        sender.sendEmail(i[0],)

    except:
        print("hata")
