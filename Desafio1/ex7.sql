SELECT * FROM Pet p
JOIN UserPet up ON p.id = up.petId
JOIN User u ON u.id = up.userId
WHERE u.id = "1571fbb8-50dc-467f-9c90-1687b2ed1aa6"