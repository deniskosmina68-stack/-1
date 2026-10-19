from app_info import show_info
from user_tools import generate_user
from math_tools import calculate
from date_tools import show_date
from web_tools import check_url
from table_tools import show_table
from json_tools import create_json
from qr_tools import create_qr
from slug_tools import create_slug
from progress_tools import show_progress
from path_tools import show_files

def main():
    show_info()
    generate_user()
    calculate()
    show_date()
    check_url()
    show_table()
    create_json()
    create_qr()
    create_slug()
    show_progress()
    show_files()

if __name__ == "__main__":
    main()
