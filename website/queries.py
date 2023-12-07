query_driver_standings = """
    WITH podiumsCTE AS (
        SELECT res.driverId,
        COUNT(CASE WHEN position = 1 THEN 1 END) as first_place_count,
        COUNT(CASE WHEN position = 2 THEN 1 END) as second_place_count,
        COUNT(CASE WHEN position = 3 THEN 1 END) as third_place_count
        FROM results res
        INNER JOIN races ra ON ra.raceId = res.raceId
        INNER JOIN drivers d ON d.driverId = res.driverId
        WHERE ra.year = 2023
        GROUP BY res.driverId
    )
    SELECT
        ROW_NUMBER() OVER (ORDER BY MAX(ds.points) DESC, MAX(ds.wins) DESC) AS 'rank',
        CONCAT(d.forename, ' ', d.surname) AS 'driver',
        MAX(CAST(ds.points AS INT)) AS 'points',
        MAX(ds.wins) AS 'wins',
        (p.first_place_count + p.second_place_count + p.third_place_count) AS 'podiums'
    FROM driverStandings ds
    INNER JOIN podiumsCTE p ON p.driverId = ds.driverId
    INNER JOIN drivers d ON d.driverId = ds.driverId
    INNER JOIN races r ON r.raceId = ds.raceId
    WHERE r.year = 2023
    GROUP BY d.driverId
    ORDER BY 1;
"""

query_constructor_standings = """
    WITH podiumsCTE AS (
        SELECT res.constructorId,
        COUNT(CASE WHEN position = 1 THEN 1 END) as first_place_count,
        COUNT(CASE WHEN position = 2 THEN 1 END) as second_place_count,
        COUNT(CASE WHEN position = 3 THEN 1 END) as third_place_count
        FROM results res
        INNER JOIN races ra ON ra.raceId = res.raceId
        INNER JOIN constructors c ON c.constructorId = res.constructorId
        WHERE ra.year = 2023
        GROUP BY res.constructorId
    )
    SELECT
        ROW_NUMBER() OVER (ORDER BY MAX(cs.points) DESC, MAX(cs.wins) DESC) AS 'rank',
        c.name AS 'constructor',
        MAX(CAST(cs.points AS INT)) AS 'points',
        MAX(cs.wins) AS 'wins',
        (p.first_place_count + p.second_place_count + p.third_place_count) AS 'podiums'
    FROM constructorStandings cs
    INNER JOIN podiumsCTE p ON p.constructorId = cs.constructorId
    INNER JOIN constructors c ON c.constructorId = cs.constructorId
    INNER JOIN races r ON r.raceId = cs.raceId
    WHERE r.year = 2023
    GROUP BY c.constructorId
    ORDER BY 1;
"""