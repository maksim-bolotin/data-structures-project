class Node:

    def __init__(self, data, next_node):
        """Конструктор класса Node"""
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.all = []

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data, self.head)
        self.head = node
        self.all.append(data)
        if self.tail is None:
            self.tail = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data, None)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node
        self.all.append(data)

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return "None"

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.strip()
