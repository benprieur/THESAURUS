# CREATE DATABASE THESAURUS_DB
# USE THESAURUS_DB
DATABASE = "THESAURUSDB"

# CREATE USER 'thesaurus'@'localhost' IDENTIFIED BY 'thesauruspwd';
# GRANT ALL PRIVILEGES ON * . * TO 'thesaurus'@'localhost';
USER = "thesaurus"
PASSWORD = "thesauruspwd"
HOST = "localhost"

TABLES = {}
TABLES['TUSER'] = (
    " CREATE TABLE IF NOT EXISTS TUSER (" 
    " id INT(10) unsigned NOT NULL AUTO_INCREMENT," 
    " name VARCHAR(200) NOT NULL," 
    " PRIMARY KEY(id)," 
    " isIP BOOLEAN DEFAULT FALSE," 
    " UNIQUE KEY name (name)" 
    " ) ENGINE=InnoDB;")

TABLES['TTHESAURUS'] = (
    " CREATE TABLE IF NOT EXISTS TTHESAURUS ("
    " id INT(10) unsigned NOT NULL AUTO_INCREMENT,"
    " name VARCHAR(200) NOT NULL,"
    " PRIMARY KEY(id),"
    " creationDateTime DATETIME,"
    " UNIQUE KEY name (name)"
    " ) ENGINE=InnoDB;")

TABLES['TEDIT'] = (
    " CREATE TABLE IF NOT EXISTS TEDIT ("
    " id INT(10) unsigned NOT NULL AUTO_INCREMENT,"
    " name VARCHAR(200) NOT NULL,"
    " PRIMARY KEY(id),"
    " code VARCHAR(200),"
    " instant DATETIME,"
    " editSize INT(10),"
    " idThesaurus INT(10) unsigned,"
    " idUser INT(10) unsigned,"
    " UNIQUE KEY name (code),"
    " CONSTRAINT fk_id_thesaurus FOREIGN KEY(idThesaurus) REFERENCES TTHESAURUS(id),"
    " CONSTRAINT fk_id_user FOREIGN KEY(idUser) REFERENCES TUSER(id)"
    " ) ENGINE=InnoDB; ")

TABLES['TUTILS'] = (
    " CREATE TABLE IF NOT EXISTS TUTILS ("
    " lastUpdate DATETIME"
    " ) ENGINE=InnoDB; ")