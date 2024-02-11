import pikepdf

def crack_pdf_password(pdf_path):
    password = 0
    while True:
        password = int(password) + 1
        password = str(password)
        try:
            pdf = pikepdf.open(pdf_path, password=password)
            print(f'Password found {password}')
            return password
        except:
            print(password)

file_path = 'mrlwitwma.pdf'
crack_pdf_password(file_path)