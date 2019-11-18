

rm -rf /usr/local/var/postgres && initdb /usr/local/vacr/postgres -E utf8 && pg_ctl -D /usr/local/var/postgres -l logfile start

pg_ctl -D /usr/local/var/postgres stop -s -m fast     

python3 -m pip install --user virtualenv

python3 -m venv venv

source venv/bin/activate

deactivate (edited) 

pip install

pip install --upgrade pip

# sudo mkdir /usr/local/var/postgres
# sudo chmod 775 /usr/local/var/postgres
# sudo chown halbaird /usr/local/var/postgres
# initdb /usr/local/var/postgres