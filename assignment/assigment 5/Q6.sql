CREATE DATABASE iot_data;
USE iot_data;

CREATE TABLE sensor_readings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    temperature FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO sensor_readings (temperature, humidity)
VALUES
(28.5, 60.2),
(22.0, 55.0),
(19.8, 70.1),
(30.2, 65.4),
(18.4, 75.0);

SELECT * FROM sensor_readings;

SELECT * 
FROM sensor_readings
WHERE temperature < 20;

SELECT * 
FROM sensor_readings
WHERE humidity < 60;

SELECT * 
FROM sensor_readings
WHERE temperature < 20 AND humidity < 65;

