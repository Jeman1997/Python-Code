class Rectangle:
    def __init__(self,wid,hei):
        self.width  = wid
        self.height = hei
    def set_width(self,new_wid):
        self.width  = new_wid
    def set_height(self,new_hei):
        self.height = new_hei
    def get_area(self):
        return (self.width * self.height)
    def get_perimeter(self):
        return ((2*self.width)+(2*self.height))
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        if self.height>50 or self.width>50:
            return 'Too big for picture'
        pic=''
        for x in range(self.height):
            pic+=('*'*self.width)+'\n'
        return pic
    def get_amount_inside(self,sq):
        sqsidehe = sq.width
        sqsidewi = sq.height
        rechei = self.height
        recwid = self.width
        if rechei>=sqsidehe and recwid>=sqsidewi:
            sqsidh = rechei/sqsidehe
            sqdidh = recwid/sqsidewi
            return int(sqsidh*sqdidh)
        else:
            return 0
        
    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width,self.height)
class Square(Rectangle):
    def __init__(self,sid):
        self.width = sid
        self.height= sid
    def set_side(self,new_sid):
        self.width=new_sid
        self.height=new_sid
    def set_width(self,new_wid):
        self.width=new_wid
        self.height=new_wid
    def set_height(self,new_height):
        self.width=new_height
        self.height=new_height
    def __str__(self):
        return 'Square(side={})'.format(self.width)


rect =Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))