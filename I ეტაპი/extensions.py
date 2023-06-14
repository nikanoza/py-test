import mimetypes

def get_media_type(file_name):
    media_type, _ = mimetypes.guess_type(file_name)
    return media_type

file_name = input("File name: ")
media_type = get_media_type(file_name)
print(media_type)