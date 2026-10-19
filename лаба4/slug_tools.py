from slugify import slugify

def create_slug():
    text = input("\nВведіть назву: ")
    print("Slug:", slugify(text))
