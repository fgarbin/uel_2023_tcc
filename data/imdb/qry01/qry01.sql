SELECT titlebasics.tconst
	,titleprincipals.tconst
	,titleprincipals.nconst
	,namebasics.primaryname
FROM titlebasics
INNER JOIN titleprincipals ON titlebasics.tconst = titleprincipals.tconst
INNER JOIN namebasics ON titleprincipals.nconst = namebasics.nconst
WHERE titlebasics.tconst = 'tt0075148'
