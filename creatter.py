from unidecode import unidecode
from PIL import Image, ImageDraw, ImageFont


def coupons(name,certificate: str, font_path: str):
    # adjust the position according to 
    # your sample
    text_y_position = 550 

    # opens the image
    img1 = Image.open(certificate, mode ='r')
    img = Image.new("RGB",img1.size,(255,255,255))
    img.paste(img1,mask=img1.split()[3])
    
        
    # gets the image width
    image_width = img.width
        
    # gets the image height
    image_height = img.height 

    # creates a drawing canvas overlay 
    # on top of the image
    draw = ImageDraw.Draw(img)

    # gets the font object from the 
    # font file (TTF)
    font = ImageFont.truetype(
        font_path,
        160 # change this according to your needs
    )

    # fetches the text width for 
    # calculations later on
    text_width, _ = draw.textsize(name, font = font)
    # text_width=text_width*0.5
    # print(text_width)

    draw.text(
        (
            # this calculation is done 
            # to centre the image
            
            500,
            1325
        ),
        
    name,
    font = font,
    fill="white",
    spacing=2,
    embedded_color="black")
    

    # saves the image in png format
    img.save("C:/Users/darkr/Desktop/creatcertifaket/pdff/{}.pdf".format(name))
    print(name+".pdf")
    
