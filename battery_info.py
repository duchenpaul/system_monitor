import wmi

c = wmi.WMI()
t = wmi.WMI(moniker = "//./root/wmi")

def get_battery_info():
    '''print the capacity of the battery'''
    batt_info_dict = {}
    batts1 = c.CIM_Battery(Caption = 'Portable Battery')
    for i, b in enumerate(batts1):
        # print('Battery %d Design Capacity: %d mWh' % (i, b.DesignCapacity or 0))
        batt_info_dict['DesignCapacity'] = b.DesignCapacity or 0

    batts = t.ExecQuery('Select * from BatteryFullChargedCapacity')
    for i, b in enumerate(batts):
        # print ('Battery %d Fully Charged Capacity: %d mWh' % 
        # (i, b.FullChargedCapacity))
        batt_info_dict['FullChargedCapacity'] = b.FullChargedCapacity
    return batt_info_dict



def get_battery_status():
    '''get the live info of the battery'''
    batt_info_dict = get_battery_info()
    batts = t.ExecQuery('Select * from BatteryStatus where Voltage > 0')
    for i, b in enumerate(batts):
        batt_info_dict['Tag'] = b.Tag
        batt_info_dict['Name'] = b.InstanceName
        batt_info_dict['PowerOnline'] = b.PowerOnline
        batt_info_dict['Discharging'] = b.Discharging
        batt_info_dict['Charging'] = b.Charging
        batt_info_dict['Voltage'] = b.Voltage
        batt_info_dict['DischargeRate'] = 0 if b.DischargeRate < 0 else b.DischargeRate
        batt_info_dict['ChargeRate'] = b.ChargeRate
        batt_info_dict['RemainingCapacity'] = b.RemainingCapacity
        batt_info_dict['Active'] = b.Active
        batt_info_dict['Critical'] = b.Critical
    return batt_info_dict


if __name__ == '__main__':
    print(get_battery_status())