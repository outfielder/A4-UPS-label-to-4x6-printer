from pdf2image import convert_from_path
pages = convert_from_path('pdf_file', 500)

# Saving pages in jpeg format

for page in pages:
    page.save('out.jpg', 'JPEG')
