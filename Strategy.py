class ImageDecoder:
    @staticmethod
    def decode(filename):
        pass


class PNGImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print('Формат изображения: PNG')


class JPEGImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print('Формат изображения: JPEG')


class GIFImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print('Формат изображения: GIF')


class Image:
    @classmethod
    def open(cls, filename):
        ext = filename.rsplit('.', 1)[-1]
        if ext == 'png':
            decoder = PNGImageDecoder
        elif ext in ('jpg', 'jpeg'):
            decoder = JPEGImageDecoder
        elif ext == 'gif':
            decoder = GIFImageDecoder
        else:
            raise RuntimeError('Невозможно опеределить формат файла %s' % filename)

        byterange = decoder.decode(filename)
        
        return cls(byterange, filename)

    def __init__(self, byterange, filename):
        self._byterange = byterange
        self._filename = filename


Image.open('picture.png')
Image.open('picture.jpg')
Image.open('picture.gif')