def longest_word(some_list):
    length_list = [len(some_list[i]) for i in range(len(some_list))]
    print("Longest word in list ",some_list,": ",some_list[length_list.index(max(length_list))])

meow = ['meow', 'meooooow', 'mr', 'mrr']
longest_word(meow)