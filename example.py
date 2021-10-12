from IPQualityScore.DBReader import DBReader

u = DBReader("IPQualityScore-IP-Reputation-Database-IPv4.ipqs").Fetch("8.8.0.0")
print(u.IsProxy())