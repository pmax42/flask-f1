DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(10) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add missing cols to drivers
ALTER TABLE drivers
ADD COLUMN country_iso VARCHAR(2),
ADD COLUMN constructor_id INT AFTER driverRef,
ADD FOREIGN KEY (constructor_id) REFERENCES constructors(constructorId);

-- Add missing cols to constructors
ALTER TABLE constructors
ADD COLUMN color VARCHAR(7),
ADD COLUMN image_url VARCHAR(255),
ADD COLUMN foundation_year INT,
ADD COLUMN team_director VARCHAR(255),
ADD COLUMN logo VARCHAR(255),
ADD COLUMN country_iso VARCHAR(2), -- We could have created a new table for countries, but it's not necessary for this project
ADD COLUMN championships_won INT;


-- Add data to new cols
SET SQL_SAFE_UPDATES = 0; -- Disable safe mode

-- Add data to drivers
UPDATE drivers
SET country_iso = CASE
    WHEN nationality = 'British' THEN 'gb'
    WHEN nationality = 'Mexican' THEN 'mx'
    WHEN nationality = 'German' THEN 'de'
    WHEN nationality = 'Finnish' THEN 'fi'
    WHEN nationality = 'Danish' THEN 'dk'
    WHEN nationality = 'Spanish' THEN 'es'
    WHEN nationality = 'French' THEN 'fr'
    WHEN nationality = 'Australian' THEN 'au'
    WHEN nationality = 'Dutch' THEN 'nl'
    WHEN nationality = 'Canadian' THEN 'ca'
    WHEN nationality = 'Japanese' THEN 'jp'
    WHEN nationality = 'Monegasque' THEN 'mc'
    WHEN nationality = 'American' THEN 'us'
    WHEN nationality = 'Chinese' THEN 'cn'
    WHEN nationality = 'Thai' THEN 'th'
END,
constructor_id = CASE
    WHEN driverRef IN ('hamilton', 'russell') THEN (SELECT constructorId FROM constructors WHERE constructorRef = 'mercedes')
    WHEN driverRef IN ('max_verstappen', 'perez') THEN (SELECT constructorId FROM constructors WHERE constructorRef = 'red_bull')
    WHEN driverRef IN ('leclerc', 'sainz') THEN (SELECT constructorId FROM constructors WHERE constructorRef = 'ferrari')
    WHEN driverRef IN ('bottas', 'zhou') THEN (SELECT constructorId FROM constructors WHERE constructorRef = 'alfa')
    WHEN driverRef IN ('norris', 'piastri') THEN (SELECT constructorId FROM constructors WHERE constructorRef = 'mclaren')
    WHEN driverRef IN ('ocon', 'gasly') THEN (SELECT constructorId FROM constructors WHERE constructorRef = 'alpine')
    WHEN driverRef IN ('tsunoda', 'ricciardo') THEN (SELECT constructorId FROM constructors WHERE constructorRef = 'alphatauri')
    WHEN driverRef IN ('stroll', 'alonso') THEN (SELECT constructorId FROM constructors WHERE constructorRef = 'aston_martin')
    WHEN driverRef IN ('kevin_magnussen', 'hulkenberg') THEN (SELECT constructorId FROM constructors WHERE constructorRef = 'haas')
    WHEN driverRef IN ('albon', 'sargeant') THEN (SELECT constructorId FROM constructors WHERE constructorRef = 'williams')
END;

-- Add data to constructors
UPDATE constructors
SET image_url = CONCAT('images/cars/', constructorRef, '.avif'),
color = CASE
    WHEN constructorRef = 'mclaren' THEN '#F58020'
    WHEN constructorRef = 'mercedes' THEN '#6CD3BF'
    WHEN constructorRef = 'red_bull' THEN '#3671C6'
    WHEN constructorRef = 'ferrari' THEN '#F91536'
    WHEN constructorRef = 'williams' THEN '#37BEDD'
    WHEN constructorRef = 'alpine' THEN '#2293D1'
    WHEN constructorRef = 'alphatauri' THEN '#5E8FAA'
    WHEN constructorRef = 'haas' THEN '#B6BABD'
    WHEN constructorRef = 'aston_martin' THEN '#358C75'
    WHEN constructorRef = 'alfa' THEN '#C92D4B'
END,
foundation_year = CASE
    WHEN constructorRef = 'mclaren' THEN 1963
    WHEN constructorRef = 'mercedes' THEN 1954
    WHEN constructorRef = 'red_bull' THEN 2005
    WHEN constructorRef = 'ferrari' THEN 1950
    WHEN constructorRef = 'williams' THEN 1977
    WHEN constructorRef = 'alpine' THEN 1977
    WHEN constructorRef = 'alphatauri' THEN 2006
    WHEN constructorRef = 'haas' THEN 2016
    WHEN constructorRef = 'aston_martin' THEN 1991
    WHEN constructorRef = 'alfa' THEN 1950
END,
team_director = CASE
    WHEN constructorRef = 'mclaren' THEN 'Andrea Stella'
    WHEN constructorRef = 'mercedes' THEN 'Toto Wolff'
    WHEN constructorRef = 'red_bull' THEN 'Christian Horner'
    WHEN constructorRef = 'ferrari' THEN 'Frederic Vasseur'
    WHEN constructorRef = 'williams' THEN 'James Vowlves'
    WHEN constructorRef = 'alpine' THEN 'Bruno Famin'
    WHEN constructorRef = 'alphatauri' THEN 'Franz Tost'
    WHEN constructorRef = 'haas' THEN 'Guenther Steiner'
    WHEN constructorRef = 'aston_martin' THEN 'Mike Krack'
    WHEN constructorRef = 'alfa' THEN 'Andreas Seidl'
END,
logo = CONCAT('images/logos/', constructorRef, '.png'),
country_iso = CASE
    WHEN constructorRef = 'mclaren' THEN 'gb'
    WHEN constructorRef = 'mercedes' THEN 'de'
    WHEN constructorRef = 'red_bull' THEN 'at'
    WHEN constructorRef = 'ferrari' THEN 'it'
    WHEN constructorRef = 'williams' THEN 'gb'
    WHEN constructorRef = 'alpine' THEN 'fr'
    WHEN constructorRef = 'alphatauri' THEN 'it'
    WHEN constructorRef = 'haas' THEN 'us'
    WHEN constructorRef = 'aston_martin' THEN 'gb'
    WHEN constructorRef = 'alfa' THEN 'ch'
END,
championships_won = CASE
    WHEN constructorRef = 'mclaren' THEN 8
    WHEN constructorRef = 'mercedes' THEN 8
    WHEN constructorRef = 'red_bull' THEN 6
    WHEN constructorRef = 'ferrari' THEN 16
    WHEN constructorRef = 'williams' THEN 9
    WHEN constructorRef = 'alpine' THEN 0
    WHEN constructorRef = 'alphatauri' THEN 0
    WHEN constructorRef = 'haas' THEN 0
    WHEN constructorRef = 'aston_martin' THEN 0
    WHEN constructorRef = 'alfa' THEN 0
END;

-- Enable safe mode
SET SQL_SAFE_UPDATES = 1;