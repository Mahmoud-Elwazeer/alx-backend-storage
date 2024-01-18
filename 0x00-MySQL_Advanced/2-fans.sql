-- ranks country origins of bands, ordered by the number of (non-unique) fans

-- for store in temp table
-- CREATE TEMPORARY TABLE temp_band_fans AS
-- SELECT
--     origin,
--     SUM(fans) AS nb_fans
-- FROM
--     metal_bands
-- GROUP BY
--     origin
-- ORDER BY
--     nb_fans
--     DESC

select origin, SUM(fans) nb_fans from `metal_bands` group by origin ORDER BY nb_fans DESC;
