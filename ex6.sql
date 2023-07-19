DELETE FROM Pet P
JOIN UserPet up ON p.id = up.petId 
JOIN User u ON u.id = up.userId
WHERE p.type = 'parrot' and u.id = "1571fbb8-50dc-467f-9c90-1687b2ed1aa6"
