--DROP INDEX idx_titleprincipals_tconst;
--DROP INDEX idx_titleprincipals_nconst;
--CREATE INDEX idx_titleprincipals_tconst ON public.titleprincipals (tconst);
--CREATE INDEX idx_titleprincipals_nconst ON public.titleprincipals (nconst);

SELECT tb.tconst, tp.tconst, tp.nconst, nb.primaryname
FROM titlebasics tb
INNER JOIN titleprincipals tp ON tb.tconst = tp.tconst
INNER JOIN namebasics nb ON tp.nconst = nb.nconst
WHERE tb.tconst = 'tt0075148';