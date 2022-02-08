from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.current_page = 0
        self.slots = 4
        self.photos = [[] for x in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        page = ceil(photos_count / 4)
        return cls(page)

    def add_photo(self, label: str):
        for p, page in enumerate(self.photos):
            if len(page) < 4:
                self.photos[p].append(label)
                return f'{label} photo added successfully on page {p + 1} slot {len(page)}'
        return 'No more free slots'

    def display(self):
        result = '-' * 11
        for page in self.photos:
            result += f'\n{" ".join(["[]" for _ in page])}'
            result += f'\n{"-" * 11}'
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())


'''
baby photo added successfully on page 1 slot 1
first grade photo added successfully on page 1 slot 2
eight grade photo added successfully on page 1 slot 3
party with friends photo added successfully on page 1 slot 4

[['baby', 'first grade', 'eight grade', 'party with friends'], []]
prom photo added successfully on page 2 slot 1
wedding photo added successfully on page 2 slot 2
-----------
[] [] [] []
-----------
[] []
-----------
'''
