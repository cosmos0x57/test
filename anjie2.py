# python 3.6 way is shorter
from pathlib import Path

# do you know the basename of the file you just read?
filename_xls = 'file123'
# python 3.6 way is shorter
from pathlib import Path

# do you know the basename of the file you just read?
filename_xls = 'file123'

# is cell read as string?
cell_content_str = """select ip.item_code , ip.gla_code_ar ,r.ruleit_text LCSPAINTSZ 
from item i , itemplant ip , ruleit r where i.item_code = ip.item_code 
and ip.plant_code = '14' and i.item_active = 1 --and i.item_code = '457332' 
and i.item_code = r.item_code and r.urule_code = 'LCSPAINTSZ'"""

def make_sql_filename(basename: str):
    return f'{basename}.sql'

def write_to_sql_file(content: str, basename: str):
    Path(make_sql_filename(basename)).write_text(content)

if __name__ == '__main__':
    write_to_sql_file(cell_content_str, filename_xls)
# is cell read as string?
cell_content_str = """select ip.item_code , ip.gla_code_ar ,r.ruleit_text LCSPAINTSZ 
from item i , itemplant ip , ruleit r where i.item_code = ip.item_code 
and ip.plant_code = '14' and i.item_active = 1 --and i.item_code = '457332' 
and i.item_code = r.item_code and r.urule_code = 'LCSPAINTSZ'"""

def make_sql_filename(basename: str):
    return f'{basename}.sql'

def write_to_sql_file(content: str, basename: str):
    Path(make_sql_filename(basename)).write_text(content)

if __name__ == '__main__':
    write_to_sql_file(cell_content_str, filename_xls)