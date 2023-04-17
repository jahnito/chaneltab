import sqlite3


def tech_possible(db: str) -> dict:
    '''
    Функция возвращает словарь где ключ id адреса, а значения кортеж (услуга, тип подключения)
    {1: ('VPN', 'SHDSL')}
    '''
    result = {}
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("""SELECT technical_possibility.object_id, technical_possibility.service, type_phys_channel.name
                    FROM
                    technical_possibility, type_phys_channel
                    WHERE
                    type_phys_channel.id = technical_possibility.type_phys_channel""")
    for id, service, type in cursor:
        if result.get(id):
            result[id].append((service, type))
        else:
            result[id] = [(service, type)]
    return result


def get_addresses(db: str) -> list:
    '''
    Вывод всех адресов на главной странице
    '''
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("""SELECT region.name, address.area, address.city, address.street, address.building, areas.area_name, address.id
                    FROM
                    address, areas, region
					WHERE
					address.area_id = areas.id
					AND
					region.id = address.region_id""")
    return [ i for i in cursor ]


def get_areas(db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('''SELECT areas.id, areas.area_name FROM areas ORDER BY areas.area_name''')
    return [ (i[0], i[1]) for i in cursor ]


def get_regions(db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('''SELECT region.id, region.name FROM region ORDER BY region.name''')
    return [ (i[0], i[1]) for i in cursor ]


def add_new_address(db, addr_data: dict):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('''SELECT count() FROM address
                    WHERE area = ? 
                    AND city = ? 
                    AND street = ? 
                    AND building = ? 
                    AND region_id = ? 
                    AND area_id = ?
                    ''', [addr_data.get('area'), addr_data.get('city'), addr_data.get('street'),
                        addr_data.get('building'), addr_data.get('region'), addr_data.get('area_id')])
    if cursor.fetchone()[0] > 0 :
        return 'Объект уже существует!'
    else:
        cursor.execute('''INSERT INTO address (area, city, street, building, region_id, area_id )
                                    VALUES ( ?, ?, ?, ?, ?, ?)''', [addr_data.get('area'),
                                    addr_data.get('city'), addr_data.get('street'),
                                    addr_data.get('building'), addr_data.get('region'), 
                                    addr_data.get('area_id')])
        connection.commit()
        return 'Объект добавлен!'
