# test_portalledger.py
"""
Tests for PortalLedger module.
"""

import unittest
from portalledger import PortalLedger

class TestPortalLedger(unittest.TestCase):
    """Test cases for PortalLedger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PortalLedger()
        self.assertIsInstance(instance, PortalLedger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PortalLedger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
