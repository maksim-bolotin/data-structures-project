class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self, head=None, tail=None):
        """Конструктор класса Queue"""
        self.all = []
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)
        if self.head is None:
            self.head = node
            self.tail = node
            self.all.append(data)
        else:
            self.tail.next_node = node
            self.tail = node
            self.all.append(data)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.all:
            removed_value = self.all.pop(0)
            return removed_value
        else:
            return None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        str_all = '\n'.join(map(str, self.all))
        return str_all
