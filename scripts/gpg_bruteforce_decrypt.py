from datetime import timedelta, date
import hashlib
import os

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2021, 01, 01)
end_dt = date(2021, 06, 07)

for dt in daterange(start_dt, end_dt):
    string= dt.strftime("%Y-%m-%d") + " bigtent"
    encoded=string.encode()
    result = hashlib.sha256(encoded)
    os.system("echo "+result.hexdigest()+" | gpg --output firefox.log.gz --batch --yes --passphrase-fd 0 --decrypt firefox.log.gz.gpg ")
    os.system("echo "+result.hexdigest()+" | gpg --output signal.log --batch --yes --passphrase-fd 0 --decrypt signal.log.gpg ")
