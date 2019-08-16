# CREATE DATABASE THESAURUS_DB
# USE THESAURUS_DB
DATABASE = "THESAURUSDB"

# CREATE USER 'thesaurus'@'localhost' IDENTIFIED BY 'thesauruspwd';
# GRANT ALL PRIVILEGES ON * . * TO 'thesaurus'@'localhost';
USER = "thesaurus"
PASSWORD = "thesauruspwd"
HOST = "localhost"

TABLES = {}
TABLES['User'] = (
    " CREATE TABLE IF NOT EXISTS User (" 
    " id INT unsigned NOT NULL AUTO_INCREMENT," 
    " name VARCHAR(200) NOT NULL," 
    " PRIMARY KEY(id)," 
    " name VARCHAR(200)," 
    " isIP INTEGER DEFAULT 0," 
    " UNIQUE KEY name (name)" 
    " ) ENGINE=InnoDB;")

TABLES['Thesaurus'] = (
    " CREATE TABLE IF NOT EXISTS Thesaurus ("
    " id INT unsigned NOT NULL AUTO_INCREMENT,"
    " name VARCHAR(200) NOT NULL,"
    " PRIMARY KEY(id),"
    " creationDateTime DATETIME,"
    " UNIQUE KEY name (name)"
    " ) ENGINE=InnoDB;")

TABLES['Edit'] = (
    " CREATE TABLE IF NOT EXISTS Edit ("
    " id INT unsigned NOT NULL AUTO_INCREMENT,"
    " name VARCHAR(200) NOT NULL,"
    " PRIMARY KEY(id),"
    " code VARCHAR(200),"
    " instant DATETIME,"
    " editSize INT,"
    " idThesaurus INT,"
    " idUser INT,"
    " UNIQUE KEY name (code),"
    " CONSTRAINT fk_id_thesaurus FOREIGN KEY (idThesaurus)"
    " REFERENCES Thesaurus(id) ON DELETE CASCADE,"
    " CONSTRAINT fk_id_User FOREIGN KEY (idUser)"
    " REFERENCES User(id) ON DELETE CASCADE"
    " ) ENGINE=InnoDB; ")