
DROP INDEX ix_titlebasics_tconst;
DROP INDEX ix_titleepisode_parenttconst;
DROP INDEX ix_titleepisode_seasonnumber_episodenumber;

/*
CREATE INDEX ix_titlebasics_tconst ON public.titlebasics (tconst);
CREATE INDEX ix_titleepisode_parenttconst ON public.titleepisode (parenttconst);
CREATE INDEX ix_titleepisode_seasonnumber_episodenumber ON public.titleepisode (seasonnumber, episodenumber);
*/
-- BARD
/*
select titlebasics.*, titleepisode.seasonnumber, titleepisode.episodenumber
from titlebasics
join lateral (
    select tconst, seasonnumber, episodenumber
    from titleepisode
    where parenttconst = 'tt0108778'
    order by seasonnumber, episodenumber
) titleepisode on titlebasics.tconst = titleepisode.tconst;
*/
-- Original
/*
select * from titlebasics
where titlebasics.tconst in (select titleepisode.tconst from titleepisode 
where titleepisode.parenttconst = 'tt0108778'
order by titleepisode.seasonnumber, titleepisode.episodenumber)
*/