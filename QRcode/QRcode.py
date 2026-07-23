#qrcode simples
import qrcode

imagem = qrcode.make('https://www.instagram.com/amordemae_boloss?igsh=MWZubzd1aDM4enNkYQ==')
imagem.save('qrcode.png')



#qrcode com imagem
from qrcode.image.styledpil import StyledPilImage
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('https://www.instagram.com/amordemae_boloss?igsh=MWZubzd1aDM4enNkYQ==')

imagem = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path='logo.png'
)

imagem.save('qr_logo_insta.png')

#vários qrcode

redes = {
    'Instagram' : 'https://www.instagram.com/amordemae_boloss?igsh=MWZubzd1aDM4enNkYQ==',
    'Whathsapp' : 'https://wa.me/5544998370432?'
}

for rede, link in redes.items():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(link)

    imagem = qr.make_image(
        image_factory=StyledPilImage,
        embeded_image_path='logo.png'
    )

    imagem.save(f'{rede}.png')