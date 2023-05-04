from pdf_mail import sendpdf
def sendEmail(name,mail):
    k=sendpdf("sauiha@sakarya.edu.tr",
        mail,
        "jjycmpvmsxaqymnw",
        "IHA",
        "Etkinliğimize katıldığınız için teşekkür ederiz," 
        "dosya açılmaz ise sonuna .pdf uzantısı ekleyerek indirebilirsiniz...",
        name,
        "C:/Users/darkr/Desktop/creatcertifaket/pdff")
        #ı have add .pdf on email_send
        #here, script is sending "certifacte.pdf"
    try:
        k.email_send()
    except:
        print("hatalı isim:",name,mail)