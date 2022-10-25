import sqlite3
import pandas as pd
con=sqlite3.connect("db.db")
wb=pd.ExcelFile('ma.xlsx')
for sheet in wb.sheet_names:
        df=pd.read_excel('ma.xlsx')
        df.to_sql(sheet,con, index=False,if_exists="replace")
con.commit()
con.close()