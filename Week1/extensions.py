def ending():
    name = input("File name: ").strip().casefold()
    parts = name.rsplit(".",1)
    if len(parts) == 1:
        return "application/octet-stream"
    elif parts[1] == "jpg":
        return ("image/jpeg")
    elif parts[1] in ["apng", "avif", "bmp", "gif", "jpeg", "png", "tiff", "webp"]:
        return ("image/" + parts[1])
    elif parts[1] == "txt":
        return "text/plain"
    elif parts[1] == "zip":
        return "application/zip"
    elif parts[1]== "pdf":
        return "application/pdf"
    else:
        return "application/octet-stream"

def main():
    print(ending())

main()
