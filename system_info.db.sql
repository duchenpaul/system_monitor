BEGIN TRANSACTION;
CREATE TABLE battery_info (record_id INTEGER PRIMARY KEY ASC AUTOINCREMENT, Tag INT, Name TEXT, PowerOnline BOOLEAN, Discharging BOOLEAN, Charging BOOLEAN, Voltage BIGINT, DischargeRate BIGINT, ChargeRate BIGINT, RemainingCapacity BIGINT, Active BOOLEAN, Critical BOOLEAN, DesignCapacity BIGINT, FullChargedCapacity BIGINT, INSERT_DATE DATETIME);
CREATE TRIGGER trg_upd_date AFTER INSERT ON battery_info FOR EACH ROW BEGIN UPDATE battery_info SET INSERT_DATE = strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime') WHERE record_id = new.record_id; END;
CREATE VIEW battery_brief AS select battery_info.Charging, 
ROUND(cast(battery_info.RemainingCapacity AS DOUBLE)  / cast(battery_info.FullChargedCapacity AS DOUBLE) * 100, 4) as percent
, INSERT_DATE from battery_info;
COMMIT;
