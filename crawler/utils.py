def __assertEquals__(transfers, other):
    assert(len(transfers) == len(other))

def click_elem_path(nb):
    return '//li[@class="page"]/a[text()==%d]' % nb

def get_positions(transfers, queries):
    positions = transfers[0].xpath(queries['positions'])
    positions = map (
        lambda t: t.text,
        filter(lambda p: p.text.strip() != "", positions)
    )
    __assertEquals__(transfers, positions)
    return positions

def get_market_values(transfers, queries):
    values = transfers[0].xpath(queries['market_values'])
    values = map(lambda t: t.strip(), values)
    __assertEquals__(transfers, values)
    return values

def get_age_season(transfers, queries):
    age_season = transfers[0].xpath(queries['age_season'])
    ages = []
    seasons = []
    for i, elem in enumerate(age_season):
        if i % 3 == 1:
            ages.append(elem)
        elif i % 3 == 2:
            seasons.append(elem)
    __assertEquals__(transfers, seasons)
    __assertEquals__(transfers, ages)
    return (ages, seasons)

def get_next_page(driver, next_page):
    next_page = str(next_page)
    elems = driver.find_elements_by_xpath('//li[@class="page"]/a')
    for elem in elems:
        if elem.text == next_page:
            break
    return elem