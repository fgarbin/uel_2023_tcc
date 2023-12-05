SELECT namebasics.nconst, namebasics.primaryname, namebasics.birthyear, namebasics.deathyear, titleprincipals.tconst, titlebasics.primarytitle
FROM namebasics 
INNER JOIN titleprincipals ON titleprincipals.nconst = namebasics.nconst
INNER JOIN titlebasics ON titlebasics.tconst = titleprincipals.tconst
INNER JOIN titleakas ON titleakas.titleid = titlebasics.tconst
WHERE 
namebasics.birthyear is not null
and namebasics.deathyear is null
and titleakas.isoriginaltitle = '1'
order by namebasics.nconst