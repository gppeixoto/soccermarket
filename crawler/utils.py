def click_elem_path(nb):
    return '//li[@class="page"]/a[text()==%d]' % nb

def get_positions(transfers, queries):
    positions = transfers[0].xpath(queries['positions'])
    positions = map (
        lambda t: t.text,
        filter(lambda p: p.text.strip() != "", positions)
    )
    assert(len(transfers) == len(positions))
    return positions