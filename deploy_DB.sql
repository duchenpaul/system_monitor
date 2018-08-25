--
-- File generated with SQLiteStudio v3.1.1 on Sat Aug 25 17:25:38 2018
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: battery_info
DROP TABLE IF EXISTS battery_info;

CREATE TABLE battery_info (
    record_id         INTEGER  PRIMARY KEY ASC AUTOINCREMENT,
    Tag               INT,
    Name              TEXT,
    PowerOnline       BOOLEAN,
    Discharging       BOOLEAN,
    Charging          BOOLEAN,
    Voltage           BIGINT,
    DischargeRate     BIGINT,
    ChargeRate        BIGINT,
    RemainingCapacity BIGINT,
    Active            BOOLEAN,
    Critical          BOOLEAN,
    INSERT_DATE       DATETIME
);


-- Trigger: trg_upd_date
DROP TRIGGER IF EXISTS trg_upd_date;
CREATE TRIGGER trg_upd_date
         AFTER INSERT
            ON battery_info
      FOR EACH ROW
BEGIN
    UPDATE battery_info
       SET INSERT_DATE = strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime') 
     WHERE record_id = new.record_id;
END;


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
