from IPQualityScore.DBReader import DBReader

ipv4_client = DBReader("IPQualityScore-IP-Reputation-Database-IPv4.ipqs")

ipv4_record = ipv4_client.Fetch("8.8.0.0")

print(f"IPv4 Is Proxy: {ipv4_record.IsProxy()}")


ipv6_client = DBReader("IPQualityScore-IP-Reputation-Database-IPv6.ipqs")

ipv6_record = ipv6_client.Fetch("2001:4860:4860::8888")

print(f"IPv6 Is Proxy: {ipv6_record.IsProxy()}")