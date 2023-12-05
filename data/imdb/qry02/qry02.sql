select * from titlebasics
where titlebasics.tconst in (select titleepisode.tconst from titleepisode 
where titleepisode.parenttconst = 'tt0108778'
order by titleepisode.seasonnumber, titleepisode.episodenumber)