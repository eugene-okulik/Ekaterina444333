class Book:
    def __init__(self, material, have_text, title, author, number_of_pages, isbn, reserved):
        self.material = material
        self.have_text = have_text
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserved = reserved


    def result(self):
        if self.reserved:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages},'
                  f' материал: {self.material}, зарезервирована')
        else:
            print( f'Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages},'
                   f' материал: {self.material}')


class SchoolBook(Book):
    def __init__(self, material, have_text, title, author, number_of_pages, isbn, reserved, lesson_title, number_of_class, have_a_tasks):
        super().__init__(material, have_text, title, author, number_of_pages, isbn, reserved)
        self.lesson_title = lesson_title
        self.number_of_class = number_of_class
        self.have_a_tasks = have_a_tasks


    def result2(self):
        if self.reserved:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages},'
                  f' предмет: {self.lesson_title}, класс: {self.number_of_class} зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages},'
                  f' предмет: {self.lesson_title}, класс: {self.number_of_class}')


the_little_prince = Book('бумага', True, 'Маленький принц', 'Антуан де Сент-Экзюпери',
                         389, '2679483947', True )
the_lord_of_the_rings = Book('бумага', True, 'Властелин колец', 'Дж. Р.P.Толкин',
                             893, '7834728463', False )
the_master_and_margarita = Book('бумага', True, 'Мастер и Маргарита', 'Михаил Булгаков',
                                1195, '4738467429', False )
one_hundred_years_of_solitude = Book('бумага', True, 'Сто лет одиночества',
                                     'Габриель Гарсия Маркиз', 596, '5738574003',
                                     False )
crime_and_punishment =Book('бумага', True, 'Преступление и наказание', 'Федор Достоевский',
                           777, '47683892455', False )

the_little_prince.result()
the_lord_of_the_rings.result()
the_master_and_margarita.result()
one_hundred_years_of_solitude.result()
crime_and_punishment.result()

math_book = SchoolBook('бумага', True, 'Алгебра', 'Р.П. Козлов', 235,
                       '47386583653', False, 'Математика', 7, True )
chemistry_book = SchoolBook('бумага', True, 'Молекулярная химия', 'А.Ю. Вишнева',
                            321,'47348583653', False, 'Химия', 10,
                            True )
history_book = SchoolBook('бумага', True, 'История древнего мира', 'А.Г. Миров',
                          235,'27386999653', True, 'Химия', 6,
                          True )

math_book.result2()
chemistry_book.result2()
history_book.result2()
