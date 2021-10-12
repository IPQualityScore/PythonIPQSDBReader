import unittest
from IPQualityScore.DBReader import DBReader

class DBReaderMethod(unittest.TestCase):
    db_ipv4 = DBReader("IPQualityScore-IP-Reputation-Database-IPv4.ipqs").Fetch("8.8.0.0")
    
    def test_IPv4IsProxy(self):
        self.assertEqual(self.db_ipv4.IsProxy(), True)

    def test_IPv4IsVPN(self):
        self.assertEqual(self.db_ipv4.IsVPN(), True)
    
    def test_IPv4IsTOR(self):
        self.assertEqual(self.db_ipv4.IsTOR(), False)
    
    def test_IPv4IsCrawler(self):
        self.assertEqual(self.db_ipv4.IsCrawler(), False)

    def test_IPv4IsBot(self):
        self.assertEqual(self.db_ipv4.IsBot(), False)

    def test_IPv4IsBlackListed(self):
        self.assertEqual(self.db_ipv4.IsBlackListed(), False)

    def test_IPv4IsPrivate(self):
        self.assertEqual(self.db_ipv4.IsPrivate(), False)

    def test_IPv4IsMobile(self):
        self.assertEqual(self.db_ipv4.IsMobile(), False)

    def test_IPv4RecentAbuse(self):
        self.assertEqual(self.db_ipv4.RecentAbuse(), False)

    def test_IPv4HasOpenPorts(self):
        self.assertEqual(self.db_ipv4.HasOpenPorts(), False)
    
    def test_IPv4IsHostingProvider(self):
        self.assertEqual(self.db_ipv4.IsHostingProvider(), False)

    def test_IPv4ActiveVPN (self):
        self.assertEqual(self.db_ipv4.ActiveVPN(), False)

    def test_IPv4ActiveTOR(self):
        self.assertEqual(self.db_ipv4.ActiveTOR(), False)

    def test_PublicAccessPoint(self):
        self.assertEqual(self.db_ipv4.PublicAccessPoint(), True)
    
    def test_ConnectionTypeRaw(self):
        self.assertEqual(self.db_ipv4.ConnectionTypeRaw(), 3)
    
    def test_ConnectionType(self):
        self.assertEqual(self.db_ipv4.ConnectionType(), "Corporate")
    
    def test_FraudScore(self):
        self.assertEqual(self.db_ipv4.FraudScore(), 75)
    
    def test_AbuseVelocity(self):
        self.assertEqual(self.db_ipv4.AbuseVelocity(), 'none')
    
    def test_Country(self):
        self.assertEqual(self.db_ipv4.Country(), 'US')

    def test_City(self):
        self.assertEqual(self.db_ipv4.City(), 'Monroe')
    
    def test_Region(self):
        self.assertEqual(self.db_ipv4.Region(), 'Louisiana')
    
    def test_ISP(self):
        self.assertEqual(self.db_ipv4.ISP(), 'Level 3 Communications')
    
    def test_Timezone(self):
        self.assertEqual(self.db_ipv4.Timezone(), 'America/Chicago')

    def test_Latitude(self):
        self.assertEqual(self.db_ipv4.Latitude(), 32.52000045776367)
    
    def test_Longitude(self):
        self.assertEqual(self.db_ipv4.Longitude(), -92.11000061035156)
    
    def test_ASN(self):
        self.assertEqual(self.db_ipv4.ASN(), 0)

if __name__ == '__main__':
    unittest.main()