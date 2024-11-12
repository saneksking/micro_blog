# Micro Blog v0.0.1

---

Micro Blog

---

- System for develop - <a href="https://manjaro.org/" target='_blank'>Manjaro Linux</a>.

- Python version <a href='https://www.python.org/downloads/release/python-3100/' target='_blank'><strong>Python 3.12</strong></a>.

### Work with DataBase:

1. `sudo systemctl stop mysqld`
2. `sudo pacman -S mariadb libmariadbclient mariadb-clients`
3. `sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql`
4. `sudo systemctl start mariadb`
5. `sudo mysql_secure_installation`
6. `sudo systemctl restart mariadb`
7. `sudo mysql -u root -p`
8. `CREATE USER 'DB_USER'@'localhost' IDENTIFIED BY 'DB_PASSWORD';`
9. `CREATE DATABASE DB_NAME CHARACTER SET utf8 COLLATE utf8_general_ci;`
10. `GRANT ALL PRIVILEGES ON DB_NAME.* TO 'DB_USER'@'localhost';`
11. `FLUSH PRIVILEGES;`
12. `exit;`

### Install requirements:

- `pip install -r requirements.txt`

If you had a problem with `mysqlclient` try this command: `pip install mysqlclient`

### Run:

- `python manage.py runserver --settings=micro_blog.settings_dev`

### Create and update migrations:

- `python manage.py makemigrations [app_name] --settings=smicro_blog.settings_dev`
- `python manage.py migrate [app_name] --settings=micro_blog.settings_dev`
