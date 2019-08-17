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
    " userName VARCHAR(200) NOT NULL," 
    " userId INT(10) unsigned," 
    " PRIMARY KEY(id)," 
    " isIP BOOLEAN DEFAULT FALSE," 
    " UNIQUE KEY userName (userName)" 
    " ) ENGINE=InnoDB;")

TABLES['TTHESAURUS'] = (
    " CREATE TABLE IF NOT EXISTS TTHESAURUS ("
    " id INT(10) unsigned NOT NULL AUTO_INCREMENT,"
    " name VARCHAR(200) NOT NULL,"
    " PRIMARY KEY(id),"
    " creationDateTime DATETIME,"
    " UNIQUE KEY name (name)"
    " ) ENGINE=InnoDB;")

TABLES['TREVISION'] = (
    " CREATE TABLE IF NOT EXISTS TREVISION ("
    " id INT(10) unsigned NOT NULL AUTO_INCREMENT,"
    " PRIMARY KEY(id),"
    " revId INT(10),"
    " instant DATETIME,"
    " currentSize INT(10),"
    " diffSize INT(10),"
    " idThesaurus INT(10) unsigned,"
    " idUser INT(10) unsigned,"
    " UNIQUE KEY revId (revId),"
    " FOREIGN KEY(idThesaurus) REFERENCES TTHESAURUS(id),"
    " FOREIGN KEY(idUser) REFERENCES TUSER(id)"
    " ) ENGINE=InnoDB; ")

TABLES['TUTILS'] = (
    " CREATE TABLE IF NOT EXISTS TUTILS ("
    " name VARCHAR(200) NOT NULL,"
    " lastUpdate DATETIME"
    " ) ENGINE=InnoDB; ")