class Flower:
    def __init__(self, name, price, freshness, color, stem_length, avg_life):
        self.name = name
        self.price = price
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.avg_life = avg_life

    def __repr__(self):
        return (
            f'{self.name}: '
            f'цена={self.price}, '
            f'свежесть={self.freshness}, '
            f'цвет={self.color}, '
            f'длина стебля={self.stem_length}, '
            f'средняя жизнь={self.avg_life}'
        )


class Rose(Flower):
    def __init__(self, name='Роза', price=50, freshness=0.8, color='красный', stem_length=50, avg_life=7):
        super().__init__(name, price, freshness, color, stem_length, avg_life)


class Tulip(Flower):
    def __init__(self, name='Тюльпан', price=70, freshness=0.7, color='желтый', stem_length=30, avg_life=4):
        super().__init__(name, price, freshness, color, stem_length, avg_life)


class Peony(Flower):
    def __init__(self, name='Пион', price=130, freshness=0.9, color='розовый', stem_length=40, avg_life=5):
        super().__init__(name, price, freshness, color, stem_length, avg_life)


class Bouquet:
    def __init__(self, flowers=None):
        if flowers is None:
            flowers = []
        self.flowers = flowers

    def add_flower(self, flower):
        self.flowers.append(flower)

    @property
    def total_cost(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifetime(self):
        total_lifetimes = sum(flower.avg_life for flower in self.flowers)
        return int(total_lifetimes / len(self.flowers)) if self.flowers else 0

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.color)

    def sort_by_price(self):
        self.flowers.sort(key=lambda x: x.price)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda x: x.stem_length)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.freshness, reverse=True)

    def find_flowers_by_avg_life(self, min_life):
        return [flower for flower in self.flowers if flower.avg_life >= min_life]


rose = Rose()
tulip = Tulip()
peony = Peony()

bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(peony)

print('Общая стоимость:', bouquet.total_cost)
print('Средняя продолжительность жизни букета в днях:', bouquet.average_lifetime())

bouquet.sort_by_freshness()
print('Цветы отсортированы по свежести:')
for flower in bouquet.flowers:
    print(f'Цветок: {flower.name}, свежий на {flower.freshness * 100}%')

long_living_flowers = bouquet.find_flowers_by_avg_life(5)
print('Цветы с минимально долгой жизнью (больше 4 дней):')
for flower in long_living_flowers:
    print(flower.name)
