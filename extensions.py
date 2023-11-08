filename = input("File name: ")
filename = filename.strip().lower()
# array = filename.split('.')

if filename.endswith('gif'):
    print("image/gif")
elif filename.endswith('jpg'):
    print("image/jpg")
elif filename.endswith('jpeg'):
    print("image/jpeg")
elif filename.endswith('png'):
    print("image/png")
elif filename.endswith('pdf'):
    print("image/pdf")
elif filename.endswith('txt'):
    print("image/txt")
elif filename.endswith('zip'):
    print("image/zip")
else:
    print("application/octet-stream")