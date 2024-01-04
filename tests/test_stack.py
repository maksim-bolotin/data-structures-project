"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        """
        Метод, который будет вызываться перед каждым тестом
        """
        self.stack = Stack()

    def test_push_and_pop(self):
        """
        Проверка методов push и pop
        """
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test__str__(self):
        """
        Проверка метода __str__
        """
        self.assertEqual(str(self.stack), " ")
        self.stack.push(1)
        self.assertEqual(str(self.stack), " ")
