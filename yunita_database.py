#!/usr/bin/env python
# coding: utf-8

# In[13]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd =""
)

cursorObject = dataBase.cursor()
cursorObject.execute ("CREATE DATABASE D3_TI_2023")


# In[12]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd ="",
    database ="d3_ti_2023"
)

cursorObject = dataBase.cursor()

studentRecord ="""CREATE TABLE DOSEN(
               NIP VARCHAR(20) PRIMARY KEY,
               NAMA_DOSEN VARCHAR(50),
               MATA_KULIAH_YANG_DIAJAR VARCHAR(50),
               EMAIL VARCHAR(255)
               )"""



cursorObject.execute(studentRecord)
dataBase.close()
                 


# In[11]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd ="",
    database ="d3_ti_2023"
)

cursorObject = dataBase.cursor()

studentRecord ="""CREATE TABLE MAHASISWA (
                  NIM VARCHAR(10) PRIMARY KEY,
                  NAMA VARCHAR(30),
                  ALAMAT VARCHAR(255),
                  MATA_KULIAH_YANG_DIIKUTI VARCHAR(10),
                  EMAIL VARCHAR(255)
                  )"""

cursorObject.execute(studentRecord)
dataBase.close()
                  


# In[15]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd ="",
    database ="d3_ti_2023"
)

cursorObject = dataBase.cursor()

studentRecord ="""CREATE TABLE DOSEN(
               NIP VARCHAR(20) PRIMARY KEY,
               NAMA_DOSEN VARCHAR(50),
               MATA_KULIAH_YANG_DIAJAR VARCHAR(50),
               EMAIL VARCHAR(255)
               )"""



cursorObject.execute(studentRecord)
dataBase.close()
                 


# In[17]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd ="",
    database ="d3_ti_2023"
)

cursorObject = dataBase.cursor()

studentRecord ="""CREATE TABLE MATA_KULIAH(
               KODE_MATA_KULIAH VARCHAR(10),
               NAMA_MATA_KULIAH VARCHAR (50),
               WAKTU DATE,
               RUANGAN VARCHAR (10)
               )"""



cursorObject.execute(studentRecord)
dataBase.close()


# In[24]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd ="",
    database ="d3_ti_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO MAHASISWA (NIM, NAMA, ALAMAT, MATA_KULIAH_YANG_DIIKUTI, EMAIL) VALUES (%s, %s, %s, %s, %s)"
val = [("V392220001", "Yunita Putri", "Surakarta", "B12", "yunitagmail"),
       ("V392220002", "Alaysa Mutia", "Surakarta", "B13", "alaysagmail"),
       ("V392220003", "Reina Syaila", "Bogor", "B12", "reinagmail"),
       ("V392220004", "Dania Syaima", "Jakarta", "B12", "daniagmail"),
       ("V392220005", "Hana Dinia", "Malang", "B13", "hanagmail" )
       
      ]



cursorObject.executemany(sql, val)
dataBase.commit()


# In[27]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd ="",
    database ="d3_ti_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO MATA_KULIAH (KODE_MATA_KULIAH, NAMA_MATA_KULIAH, WAKTU, RUANGAN) VALUES (%s, %s, %s, %s)"
val = [("B12", "PYTHON", "JAM KE 1-4","L2R2"),
       ("B13", "BASIS DATA", "JAM KE 5-6","L2R1"),
       ("B14", "INGGRIS", "JAM KE 1-4","L2R1")
       ("B15", "JAVA", "JAM KE 1-4","L2R5")
       ("B16", " STATISTKA", "JAM KE 1-4","L2R2"),
       ("B17", "PEMROGRAMMAN WEB", "JAM KE 7-8", "L2R2"),
       ("B18", "HTML", "JAM KE 1-4","L2R9")
       
       
      ]



cursorObject.executemany(sql, val)
dataBase.commit()


# In[28]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd ="",
    database ="d3_ti_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO DOSEN (NIP, NAMA_DOSEN, MATA_KULIAH_YANG_DIAJAR, EMAIL) VALUES (%s, %s, %s, %s)"
val = [("198504242022", "Yunita Kartika", "B12", "kartikagmail"),
       ("198504242023", "Daniel Surendra", "B13", "danielgmail"),
       ("198504242024", "Adinda Rahma", "B14", "adindagmail"),
       ("198504242025", "Loefena Lorencia", "B15", "loefenagmail"),
       ("198504242026", "Ganisa Aisha", "B16", "ganishaagmail"),
       ("198504242027", "Remoe Randi", "B17", "romegmail"),
       ("198504242028", "Kevin Mitnick", "B18", "kevingmail"),
       
      ]



cursorObject.executemany(sql, val)
dataBase.commit()


# In[32]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd ="",
    database ="d3_ti_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO MATA_KULIAH (KODE_MATA_KULIAH, NAMA_MATA_KULIAH, WAKTU, RUANGAN) VALUES (%s, %s, %s, %s)"
val = [("B12", "PYTHON", "07.00-09.00","L2R2"),
       ("B13", "BASIS DATA","07.00-09.00" ,"L2R1"),
       ("B14", "INGGRIS", "12.00-14.00","L2R1"),
       ("B15", "JAVA", "07.00-09.00","L2R5"),
       ("B16", " STATISTKA", "09.00-12.00","L2R2"),
       ("B17", "PEMROGRAMMAN WEB", "07.00-09.00", "L2R2"),
       ("B18", "HTML", "09.00-12.00","L2R9")
       
       
      ]



cursorObject.executemany(sql, val)
dataBase.commit()


# In[41]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)

cursorObject = dataBase.cursor()
query = "SELECT `B12` FROM `MAHASISWA`
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)

dataBase.close()


# In[44]:


import mysql.connector

# Connect to the database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",  # Fill in your password if you have set one
    database="D3_TI_2023"
)

# Create a cursor object to execute queries
cursorObject = dataBase.cursor()

# SQL query to select data showing courses taken by students along with the respective teachers who teach them
query = """
SELECT m.NIM, m.Nama AS Nama_Mahasiswa, m.Mata_kuliah_yang_diikuti AS Mata_Kuliah,
       d.NIP, d.Nama_Dosen, Mata_Kuliah_yang_di_ajar AS Mata_Kuliah_yang_Diajar
FROM Mahasiswa m
JOIN Dosen d ON m.Mata_kuliah_yang_diikuti = Mata_Kuliah_yang_di_ajar
"""

# Execute the query
cursorObject.execute(query)

# Fetch all the results
myresult = cursorObject.fetchall()

# Display the results
for row in myresult:
    print("NIM:", row[0])
    print("Nama Mahasiswa:", row[1])
    print("Mata Kuliah:", row[2])
    print("NIP Dosen:", row[3])
    print("Nama Dosen:", row[4])
    print("Mata Kuliah yang Diajar Dosen:", row[5])
    print()

# Close the database connection
dataBase.close()


# In[47]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)

cursorObject = dataBase.cursor()
query = """
    SELECT NAMA AS NAMA_MAHASISWA, MATA_KULIAH_YANG_DIIKUTI AS MATA_KULIAH,
           NAMA_DOSEN AS NAMA_DOSEN
    FROM Mahasiswa
    JOIN Mata_Kuliah ON MATA_KULIAH_YANG_DIIKUTI = KODE_MATA_KULIAH
    JOIN Dosen ON MATA_KULIAH_YANG_DIAJAR = MATA_KULIAH_YANG_DIAJAR
"""
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)

dataBase.close()


# In[ ]:




