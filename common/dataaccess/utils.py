
def build_pagination(page_number, page_size):
    offset = page_number*page_size
    offset_statement = " offset "+str(offset)+" limit "+str(page_size)

    return offset_statement