/*
DROP INDEX idx_titlebasics_tconst;
DROP INDEX idx_titleepisode_tconst;
DROP INDEX idx_titleepisode_parenttconst;
*/
/*
CREATE INDEX idx_titlebasics_tconst ON public.titlebasics(tconst);
CREATE INDEX idx_titleepisode_tconst ON public.titleepisode(tconst);
CREATE INDEX idx_titleepisode_parenttconst ON public.titleepisode(parenttconst);
*/
-- CHATGPT
/*
SELECT tb.*
FROM titlebasics tb
JOIN titleepisode te ON tb.tconst = te.tconst
WHERE te.parenttconst = 'tt0108778'
ORDER BY te.seasonnumber, te.episodenumber;
*/


-- Original
/*
select * from titlebasics
where titlebasics.tconst in (select titleepisode.tconst from titleepisode 
where titleepisode.parenttconst = 'tt0108778'
order by titleepisode.seasonnumber, titleepisode.episodenumber)
*/