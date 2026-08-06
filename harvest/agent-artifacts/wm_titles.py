import urllib.parse
titles = [
'File:Armeniaca.jpg',
'File:Illustration from Pomona Italiana Giorgio Gallesio by rawpixel00010.jpg',
'File:A peach plant (Prunus persica); flowering and fruiting stems Wellcome V0044759.jpg',
"File:Nectarine Peach, Princess of Wales, Sea Eagle by May Rivers for The fruit grower's guide.jpg",
'File:Peach (PSF).png',
'File:Peach (Prunus species); fruits and leaves. Watercolour. Wellcome V0043465.jpg',
'File:Plant-Forms Ornamentally Treated - Peach Blossom by Boston Public Library.jpg',
'File:Illustration Prunus persica clean.jpg',
'File:An olive plant (Olea europea); fruiting branch. Coloured lit Wellcome V0044586.jpg',
'File:Cherry-time LCCN90715900.jpg',
'File:Montmorency, one of Three best cherries (cropped).jpg',
'File:Napoleon Bigarreau, one of Three best cherries (cropped).jpg',
'File:Three best cherries.jpg',
'File:Vintage illustrations by Miss May Rivers digitally enhanced by rawpixel 126.jpg',
]
titlestr = '|'.join(titles)
url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=' + urllib.parse.quote(titlestr) + '&prop=imageinfo&iiprop=url|extmetadata&format=json'
print(url)
