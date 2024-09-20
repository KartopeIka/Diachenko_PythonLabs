import random

class Store:
    def __init__(self, goods: set, name):
        self.goods = set([random.choice(list(goods)) for i in range(0, random.randrange(1, len(goods) - 1, 1))])
        self.name = name + 1

    def __str__(self):
        return "Асортимент магазину "+ str(self.name) +": " + str(self.goods) +"\n"

def goods_nowhere_to_find (goods:set, store_ammount):
    string_to_print = "Набір товарів: " + str(goods) +"\n\n"
    stores_list = []
    all_stores_goods ={}
    for i in range(store_ammount):
        stores_list.append(Store(goods, i))
        string_to_print += str(stores_list[i])
        all_stores_goods = set(all_stores_goods).union(stores_list[i].goods)
    goods_rest = goods-all_stores_goods
    if goods_rest:
        string_to_print += "\nТовари, яких немає в жодному магазині: " + str(goods_rest)
    else:
        string_to_print += "\nУсі товари хоч десь та продаються"
    print(string_to_print)


our_goods = {"груші", "яблучкі", "бананчики", "цукєрочкі", "картопелька", "морква", "Монітор MSI PRO MP252", "свята вода 3л", "свічка церковна", "збірка пісень Олега Винника"}
our_stores_ammount = 3
goods_nowhere_to_find(our_goods, our_stores_ammount)