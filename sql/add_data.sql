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

-- Add color and image_url cols to constructors
ALTER TABLE constructors
ADD COLUMN color VARCHAR(7) AFTER name,
ADD COLUMN image_url VARCHAR(255) AFTER color;

-- Add data to new cols
SET SQL_SAFE_UPDATES = 0; -- Disable safe mode
UPDATE constructors
SET image_url = CONCAT('images/cars/', constructorRef, '.avif');
UPDATE constructors
SET color = '#F58020'
WHERE constructorRef = 'mclaren';
UPDATE constructors
SET color = '#6CD3BF'
WHERE constructorRef = 'mercedes';
UPDATE constructors
SET color = '#3671C6'
WHERE constructorRef = 'red_bull';
UPDATE constructors
SET color = '#F91536'
WHERE constructorRef = 'ferrari';
UPDATE constructors
SET color = '#37BEDD'
WHERE constructorRef = 'williams';
UPDATE constructors
SET color = '#2293D1'
WHERE constructorRef = 'alpine';
UPDATE constructors
SET color = '#5E8FAA'
WHERE constructorRef = 'alphatauri';
UPDATE constructors
SET color = '#B6BABD'
WHERE constructorRef = 'haas';
UPDATE constructors
SET color = '#358C75'
WHERE constructorRef = 'aston_martin';
UPDATE constructors
SET color = '#C92D4B'
WHERE constructorRef = 'alfa';
SET SQL_SAFE_UPDATES = 1; -- Enable safe mode

-- Create a relation between drivers and constructors
ALTER TABLE drivers
ADD COLUMN constructor_id INT AFTER driverRef,
ADD FOREIGN KEY (constructor_id) REFERENCES constructors(constructorId);

-- Add data to new col
SET SQL_SAFE_UPDATES = 0; -- Disable safe mode
UPDATE drivers
SET constructor_id = (SELECT constructorId FROM constructors WHERE constructorRef = 'mclaren')
WHERE driverRef = 'norris' OR driverRef = 'piastri';
UPDATE drivers
SET constructor_id = (SELECT constructorId FROM constructors WHERE constructorRef = 'mercedes')
WHERE driverRef = 'hamilton' OR driverRef = 'russell';
UPDATE drivers
SET constructor_id = (SELECT constructorId FROM constructors WHERE constructorRef = 'red_bull')
WHERE driverRef = 'verstappen' OR driverRef = 'perez';
UPDATE drivers
SET constructor_id = (SELECT constructorId FROM constructors WHERE constructorRef = 'ferrari')
WHERE driverRef = 'leclerc' OR driverRef = 'sainz';
UPDATE drivers
SET constructor_id = (SELECT constructorId FROM constructors WHERE constructorRef = 'williams')
WHERE driverRef = 'albon' OR driverRef = 'sargeant';
UPDATE drivers
SET constructor_id = (SELECT constructorId FROM constructors WHERE constructorRef = 'alpine')
WHERE driverRef = 'gasly' OR driverRef = 'ocon';
UPDATE drivers
SET constructor_id = (SELECT constructorId FROM constructors WHERE constructorRef = 'alphatauri')
WHERE driverRef = 'tsunoda' OR driverRef = 'ricciardo';
UPDATE drivers
SET constructor_id = (SELECT constructorId FROM constructors WHERE constructorRef = 'haas')
WHERE driverRef = 'magnussen' OR driverRef = 'hulkenberg';
UPDATE drivers
SET constructor_id = (SELECT constructorId FROM constructors WHERE constructorRef = 'aston_martin')
WHERE driverRef = 'stroll' OR driverRef = 'alonso';
UPDATE drivers
SET constructor_id = (SELECT constructorId FROM constructors WHERE constructorRef = 'alfa')
WHERE driverRef = 'bottas' OR driverRef = 'zhou';
SET SQL_SAFE_UPDATES = 1; -- Enable safe mode
