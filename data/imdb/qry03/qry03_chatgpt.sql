
DROP INDEX idx_namebasics_birthdeath;
DROP INDEX idx_titleprincipals_nconst;
DROP INDEX idx_titlebasics_tconst;
DROP INDEX idx_titleakas_titleid;

/*
CREATE INDEX idx_namebasics_birthdeath ON public.namebasics (birthyear, deathyear);
CREATE INDEX idx_titleprincipals_nconst ON public.titleprincipals (nconst);
CREATE INDEX idx_titlebasics_tconst ON public.titlebasics (tconst);
CREATE INDEX idx_titleakas_titleid ON public.titleakas (titleid, isoriginaltitle);
*/
-- CHATGPT
/*
SELECT nb.nconst, nb.primaryname, nb.birthyear, nb.deathyear, tp.tconst, tb.primarytitle
FROM namebasics AS nb
INNER JOIN titleprincipals AS tp ON tp.nconst = nb.nconst
INNER JOIN titlebasics AS tb ON tb.tconst = tp.tconst
INNER JOIN titleakas AS ta ON ta.titleid = tb.tconst
WHERE nb.birthyear IS NOT NULL AND nb.deathyear IS NULL AND ta.isoriginaltitle = '1'
ORDER BY nb.nconst;
*/


-- Original
/*
SELECT namebasics.nconst, namebasics.primaryname, namebasics.birthyear, namebasics.deathyear, titleprincipals.tconst, titlebasics.primarytitle FROM namebasics INNER JOIN titleprincipals ON titleprincipals.nconst = namebasics.nconst
INNER JOIN titlebasics ON titlebasics.tconst = titleprincipals.tconst INNER JOIN titleakas ON titleakas.titleid = titlebasics.tconst
WHERE namebasics.birthyear is not null and namebasics.deathyear is null and titleakas.isoriginaltitle = '1' order by namebasics.nconst
*/