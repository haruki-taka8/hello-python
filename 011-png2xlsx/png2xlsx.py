import os
import re
from PIL import Image
import openpyxl
from openpyxl.styles import PatternFill

pngPath = ''
while (not os.path.isfile(pngPath)):
    pngPath = input('Input PNG   = ')

png = Image.open(pngPath)
print('PNG Size    = ' + str(png.width) + 'x' + str(png.height))

print()
scale = input('Output % (default 1) = ')
try:
    scale = int(scale)
except ValueError:
    scale = 1

output = input('Output XLSX          = ')
if output == '':
    output = 'png2xslx-'+re.sub(r'[\/?<>\\:*|"]', '', pngPath)+'.xlsx'
print()


# Resize image
scale = max(1, min(scale, 100))
png = png.convert("RGB")
png = png.resize((int(png.width * scale / 100), int(png.height * scale / 100)))
pixel = png.load()

xls = openpyxl.Workbook()
ws = xls.active
ws.title = re.sub(r'[\/?<>\\:*|"]', '', pngPath)

# Color everything
print('Coloring...')
for y in range(png.height):
    for x in range(png.width):
        print(str(round((y*x+x)/(png.width*png.height)*100,0))+'%')
        ws.cell(row=y+1, column=x+1).fill = PatternFill(fgColor=('FF%02x%02x%02x' % pixel[x,y]), fill_type="solid")

# Resize cells to square pixels
print('Resizing...')
for col in range(png.width):
    ws.column_dimensions[openpyxl.utils.cell.get_column_letter(col+1)].width = 0.825

for row in range(png.height):
    ws.row_dimensions[row+1].height = 4

# End
xls.save(output)
print('Saved as ' + output)
exit(0)