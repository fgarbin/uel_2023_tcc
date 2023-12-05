--DROP INDEX ix_titlebasics_tconst;
--DROP INDEX ix_titlebasics_titletype;
--DROP INDEX ix_titleprincipals_tconst;
--DROP INDEX ix_titleprincipals_nconst;
--DROP INDEX ix_namebasics_nconst;

--CREATE INDEX ix_titlebasics_tconst ON public.titlebasics (tconst);
--CREATE INDEX ix_titlebasics_titletype ON public.titlebasics (titletype);
--CREATE INDEX ix_titleprincipals_tconst ON public.titleprincipals (tconst);
--CREATE INDEX ix_titleprincipals_nconst ON public.titleprincipals (nconst);
--CREATE INDEX ix_namebasics_nconst ON public.namebasics (nconst);

select tb.tconst, tp.tconst, tp.nconst, nb.primaryname
from titlebasics tb
inner join titleprincipals tp on tb.tconst = tp.tconst
inner join namebasics nb on tp.nconst = nb.nconst
where tb.tconst = 'tt0075148';