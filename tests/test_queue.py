"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestStack(unittest.TestCase):
    def setUp(self):
        """
        Метод, который будет вызываться перед каждым тестом
        """
        self.stack = Queue()

    def test_enqueue_and_dequeue(self):
        """
        Проверка методов enqueue и dequeue
        """
        self.stack.enqueue(1)
        self.stack.enqueue(2)
        self.assertEqual(self.stack.dequeue(), 1)
        self.assertEqual(self.stack.dequeue(), 2)

    def test__str__(self):
        self.assertEqual(str(self.stack), "")
        self.stack.enqueue(1)
        self.stack.enqueue(2)
        self.assertEqual(str(self.stack), "1\n2")
