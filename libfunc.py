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
    cursor.execute("""SELECT region.name, areas.area_name, address.city, address.street, address.building, areas_owners.area_name,
       address.id, region.id, areas.id, areas_owners.id
       FROM
       address, areas_owners, region, areas
	   WHERE
	   areas.id = address.area_id
	   AND
	   areas_owners.id = address.area_owner
	   AND
	   region.id = address.region_id
       ORDER BY areas.area_name, address.city, address.street""")
    result = [ i for i in cursor ]
    connection.close()
    return result


def get_areas(db) -> list:
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('''SELECT areas.id, areas.area_name, areas.description FROM areas ORDER BY areas.area_name''')
    result = [ (i[0], i[1], i[2]) for i in cursor ]
    connection.close()
    return result


def get_area_owners(db) -> list:
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('''SELECT areas_owners.id, areas_owners.area_name FROM areas_owners ORDER BY areas_owners.area_name''')
    result = [ (i[0], i[1]) for i in cursor ]
    connection.close()
    return result


def get_regions(db) -> list:
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('''SELECT region.id, region.name FROM region ORDER BY region.name''')
    result = [ (i[0], i[1]) for i in cursor ]
    connection.close()
    return result


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
        connection.close()
        return 'Объект добавлен!'


def add_new_area(db, area_data: dict):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('''SELECT count() FROM areas
                      WHERE
                      id = ?
                      AND
                      area_name = ?''', [area_data.get('id'), area_data.get('area_name')])
    if cursor.fetchone()[0] > 0:
        return 'Район уже существует!'
    elif not area_data.get('area_name'):
        return 'ВНИМАНИЕ! Не определено наименование района!'
    else:
        try:
            cursor.execute('''INSERT INTO areas (id, area_name, description )
                                        VALUES ( ?, ?, ?)''', [area_data.get('id'),
                                        area_data.get('area_name'), area_data.get('description')])
            connection.commit()
            connection.close()
            return 'Объект добавлен!'
        except sqlite3.IntegrityError as e:
            return f'Ошибка SQL {e}'


def edit_address(db, addr_data: dict):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('''
                    UPDATE address
                    SET area_id = ?, city = ?, street = ?, building = ?, region_id = ?, area_owner = ?
                    WHERE id = ?;
                    ''', [addr_data.get('area_id'), addr_data.get('city'),
                          addr_data.get('street'), addr_data.get('building'),
                          addr_data.get('region'), addr_data.get('area_owner'),
                          addr_data.get('id')])
    connection.commit()
    connection.close()
    return "Данные об объекте обновлены!"
