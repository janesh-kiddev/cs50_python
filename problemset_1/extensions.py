k=input('File Name:')
ext=k[len(k)-4:].lower()
if ext in ['.gif','.jpg','.png']:
    print(f'image/{ext[1:]}')
elif ext in ['.zip','.pdf','.txt']:
    print(f'application/{ext[1:]}')
elif ext in ['jpeg']:
    print(f'image/{ext}')
else:
    print('application/octet-stream')
