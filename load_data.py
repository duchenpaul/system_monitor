import time

import toolkit_sqlite
import toolkit_file

import battery_info

DB_FILE = toolkit_file.script_path() + 'system_info.db'


def load_battery_info():
    battery_status_dict = battery_info.get_battery_status()
    print(battery_status_dict)


    insert_SQL = '''
INSERT INTO battery_info (
                             Tag,
                             Name,
                             PowerOnline,
                             Discharging,
                             Charging,
                             Voltage,
                             DischargeRate,
                             ChargeRate,
                             RemainingCapacity,
                             Active,
                             Critical,
                             DesignCapacity,
                             FullChargedCapacity
                         )
                         VALUES (
                             '%(Tag)s',
                             '%(Name)s',
                             '%(PowerOnline)s',
                             '%(Discharging)s',
                             '%(Charging)s',
                             '%(Voltage)s',
                             '%(DischargeRate)s',
                             '%(ChargeRate)s',
                             '%(RemainingCapacity)s',
                             '%(Active)s',
                             '%(Critical)s',
                             '%(DesignCapacity)s',
                             '%(FullChargedCapacity)s'
                         );
''' % battery_status_dict

    # print(insert_SQL)
    with toolkit_sqlite.SqliteDB(DB_FILE) as sqlitedb:
        sqlitedb.execute(insert_SQL)

if __name__ == '__main__':
    load_battery_info()