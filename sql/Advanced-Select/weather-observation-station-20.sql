SELECT round(S.LAT_N,4) mediam FROM station S 
WHERE (SELECT count(Lat_N) FROM station WHERE Lat_N < S.LAT_N ) = 
	  (SELECT count(Lat_N) FROM station WHERE Lat_N > S.LAT_N)