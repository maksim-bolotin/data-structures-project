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
        else:
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head:
            removed_value = self.head.data
            self.head = self.head.next_node
            return removed_value

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        result = []
        current_head = self.head
        while current_head:
            result.append(str(current_head.data))
            current_head = current_head.next_node
        return '\n'.join(result)
