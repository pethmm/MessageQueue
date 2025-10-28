# test_messagequeue.py
"""
Tests for MessageQueue module.
"""

import unittest
from messagequeue import MessageQueue

class TestMessageQueue(unittest.TestCase):
    """Test cases for MessageQueue class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MessageQueue()
        self.assertIsInstance(instance, MessageQueue)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MessageQueue()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
