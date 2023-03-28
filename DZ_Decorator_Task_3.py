import types
from DZ_Decorator_Task_2 import logger


@logger(path='log.txt')
def flat_generator(list_of_lists):
    for root_list in list_of_lists:
        if isinstance(root_list, list):
            yield from flat_generator(root_list)

        else:
            yield root_list


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    print('Проверка поэлементно:')
    for flat_iterator_item, check_item in zip(flat_generator(list_of_lists_2), ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']):
        assert flat_iterator_item == check_item
        print(f'{flat_iterator_item} = {check_item}')

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    print(f"\nПроверка списков:\n {list(flat_generator(list_of_lists_2))} = {['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']}")


    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()