#Первичная папка
source_dir = r"D:\Projects\saved_files"

DB_CONFIG = {
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'database': 'file_movements'
}

DEFAULT_DEST_DIRS = {
    '.txt': r"D:\Projects\sorted_files\TextFiles",
    '.pdf': r"D:\Projects\sorted_files\PDF",
    '.jpg': r"D:\Projects\sorted_files\JPEG"
}
#TODO: переписать под .env python-dotenv
