def handle_uploaded_file(f):
    with open('blog/static/images/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)