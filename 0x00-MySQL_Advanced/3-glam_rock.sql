-- a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

-- Requirements:

-- Import this table dump: metal_bands.sql.zip
-- Column names must be: band_name and lifespan (in years until 2022 - please use 2022 instead of YEAR(CURDATE()))
-- You should use attributes formed and split for computing the lifespan

-- SELECT band_name, IFNULL(split, 2020) - formed AS lifespan
-- FROM metal_bands
-- WHERE FIND_IN_SET("Glam rock", style)
-- ORDER BY lifespan DESC;

SELECT
    band_name,
    CASE
        WHEN split IS NOT NULL THEN YEAR(split) - YEAR(formed)
        ELSE 2022 - YEAR(formed)
    END AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan
    DESC;
