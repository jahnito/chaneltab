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
    cursor.execute("""SELECT region.name, areas.area_name, address.city, address.street, address.building, areas_owners.area_name, address.id
       FROM
       address, areas_owners, region, areas
	   WHERE
	   areas.id = address.area_id
	   AND
	   areas_owners.id = address.area_owner
	   AND
	   region.id = address.region_id""")
    return [ i for i in cursor ]


def get_areas(db) -> list:
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('''SELECT areas.id, areas.area_name FROM areas ORDER BY areas.area_name''')
    return [ (i[0], i[1]) for i in cursor ]


def get_area_owners(db) -> list:
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('''SELECT areas_owners.id, areas_owners.area_name FROM areas_owners ORDER BY areas_owners.area_name''')
    return [ (i[0], i[1]) for i in cursor ]


def get_regions(db) -> list:
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('''SELECT region.id, region.name FROM region ORDER BY region.name''')
    return [ (i[0], i[1]) for i in cursor ]


def add_new_address(db, addr_data: dict):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('''SELECT count() FROM address
                    WHERE area_id = ? 
                    AND city = ? 
                    AND street = ? 
                    AND building = ? 
                    AND region_id = ? 
                    AND area_owner = ?
                    ''', [addr_data.get('area_id'), addr_data.get('city'), addr_data.get('street'),
                        addr_data.get('building'), addr_data.get('region'), addr_data.get('area_owner')])
    if cursor.fetchone()[0] > 0:
        return 'Объект уже существует!'
    elif not addr_data.get('area_id'):
        return 'ВНИМАНИЕ! Не выбран район!'
    elif not addr_data.get('area_owner'):
        return 'ВНИМАНИЕ! Не выбрана принадлежность!'
    else:
        cursor.execute('''INSERT INTO address (area_id, city, street, building, region_id, area_owner )
                                    VALUES ( ?, ?, ?, ?, ?, ?)''', [addr_data.get('area_id'),
                                    addr_data.get('city'), addr_data.get('street'),
                                    addr_data.get('building'), addr_data.get('region'), 
                                    addr_data.get('area_owner')])
        connection.commit()
        return 'Объект добавлен!'
