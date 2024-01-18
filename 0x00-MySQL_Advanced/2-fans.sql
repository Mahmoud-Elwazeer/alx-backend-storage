-- ranks country origins of bands, ordered by the number of (non-unique) fans

select origin, SUM(fans) nb_fans from `metal_bands` group by origin ORDER BY nb_fans DESC;
