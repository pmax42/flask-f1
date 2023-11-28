from flask_table import Table, Col, LinkCol

class DriverStandings(Table):
    rank = Col('Rank')
    driver = Col('Driver')
    points = Col('Points')
    wins = Col('Wins')
    podiums = Col('Podiums')

class DriverStanding(object):
    def __init__(self, rank, driver, points, wins, podiums):
        self.rank = rank
        self.driver = driver
        self.points = points
        self.wins = wins
        self.podiums = podiums

query = """
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
    CONCAT(d.forename, ' ', d.surname) AS 'Driver',
    MAX(ds.points) AS 'Points',
    MAX(ds.wins) AS 'Wins',
    (p.first_place_count + p.second_place_count + p.third_place_count) AS 'Podiums'
FROM driverStandings ds
INNER JOIN podiumsCTE p ON p.driverId = ds.driverId
INNER JOIN drivers d ON d.driverId = ds.driverId
INNER JOIN races r ON r.raceId = ds.raceId
WHERE r.year = 2023
GROUP BY d.driverId
ORDER BY 2 DESC, 4 DESC;
"""

def test_get_data(db):
    standings = db.engine.execute(query)
    driver_standings = []
    for standing in standings:
        driver_standings.append(DriverStanding(standing[0], standing[1], standing[2], standing[3], standing[4]))
    print(driver_standings)