/*
DROP INDEX ix_namebasics_nconst;
DROP INDEX ix_titlebasics_tconst;
DROP INDEX ix_titleprincipals_tconst;
DROP INDEX ix_titleakas_isoriginaltitle;
*/
/*
CREATE INDEX ix_namebasics_nconst ON public.namebasics (nconst COLLATE "C" bpchar_pattern_ops);
CREATE INDEX ix_titlebasics_tconst ON public.titlebasics (tconst COLLATE "C" bpchar_pattern_ops);
CREATE INDEX ix_titleprincipals_tconst ON public.titleprincipals (tconst COLLATE "C" bpchar_pattern_ops);
CREATE INDEX ix_titleakas_isoriginaltitle ON public.titleakas (isoriginaltitle COLLATE "C" bpchar_pattern_ops);
*/
-- BARD
/*
Fail
SELECT namebasics.nconst,
       namebasics.primaryname,
       namebasics.birthyear,
       namebasics.deathyear,
       titleprincipals.tconst,
       titlebasics.primarytitle
FROM namebasics
INNER JOIN titleprincipals ON titleprincipals.nconst = namebasics.nconst
INNER JOIN titlebasics ON titlebasics.tconst = titleprincipals.tconst
WHERE namebasics.birthyear IS NOT NULL
      AND namebasics.deathyear IS NULL
      AND (SELECT COUNT(*) FROM titleakas WHERE titleakas.titleid = titlebasics.tconst AND isoriginaltitle = '1') > 0
ORDER BY namebasics.nconst;

CREATE MATERIALIZED VIEW original_titles AS
SELECT namebasics.nconst,
       namebasics.primaryname,
       namebasics.birthyear,
       namebasics.deathyear,
       titleprincipals.tconst,
       titlebasics.primarytitle
FROM namebasics
INNER JOIN titleprincipals ON titleprincipals.nconst = namebasics.nconst
INNER JOIN titlebasics ON titlebasics.tconst = titleprincipals.tconst
WHERE namebasics.birthyear IS NOT NULL
      AND namebasics.deathyear IS NULL
      AND (SELECT COUNT(*) FROM titleakas WHERE titleakas.titleid = titlebasics.tconst AND isoriginaltitle = '1') > 0;
*/
SELECT namebasics.nconst,
       namebasics.primaryname,
       namebasics.birthyear,
       namebasics.deathyear,
       titleprincipals.tconst,
       titlebasics.primarytitle
FROM namebasics
INNER JOIN titleprincipals ON titleprincipals.nconst = namebasics.nconst
INNER JOIN titlebasics ON titlebasics.tconst = titleprincipals.tconst
WHERE namebasics.birthyear IS NOT NULL
      AND namebasics.deathyear IS NULL
      AND titlebasics.primarytitle IS NOT NULL
      AND titlebasics.originaltitle IS NOT NULL
ORDER BY namebasics.nconst;

-- Original
/*
SELECT namebasics.nconst, namebasics.primaryname, namebasics.birthyear, namebasics.deathyear, titleprincipals.tconst, titlebasics.primarytitle FROM namebasics INNER JOIN titleprincipals ON titleprincipals.nconst = namebasics.nconst
INNER JOIN titlebasics ON titlebasics.tconst = titleprincipals.tconst INNER JOIN titleakas ON titleakas.titleid = titlebasics.tconst
WHERE namebasics.birthyear is not null and namebasics.deathyear is null and titleakas.isoriginaltitle = '1' order by namebasics.nconst
*/