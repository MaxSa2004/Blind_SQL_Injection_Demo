# Blind_SQL_Injection_Demo

This repo contains a small working example of a site vulnerable to blind SQL Injection and a safe non-vulnerable version.

## Prerequisites
Ensure the following are installed before running the program.

**SQLite**
```
sudo apt install sqlite3
```

**Flask**
```
pip install flask
```

## Usage
### First Run
***Do this before running the apps!***

Setup the database with the following command (only ever needs to run once):
```
python3 init_db.py
```

### Vulnerable
Start `app.py` and paste http://127.0.0.1:5000 into your browser
```
python3 app.py
```

To test search for the following (all events appear):
```
%' AND (SELECT salary FROM users WHERE username='alice_test') > 2000 --
```
Now search for (no events appear):
```
%' AND (SELECT salary FROM users WHERE username='alice_test') > 3000 --
```
We can conclude that Alice earns between 2000 and 3000. You have used Blind SQL Injection to infer information!

#### Vulnerable Code Section
```
query = f"""
        SELECT title, date, location
        FROM events
        WHERE title LIKE '%{search}%'
    """

try:
        events = connection.execute(query).fetchall()
    except Exception:
        events = []
```

### Non-Vulnerable
Start `appSAFE.py` and paste http://127.0.0.1:5000 into your browser
```
python3 appSAFE.py
```

To test search for the following (no events appear):
```
%' AND (SELECT salary FROM users WHERE username='alice_test') > 2000 --
```
Now search for (no events appear):
```
%' AND (SELECT salary FROM users WHERE username='alice_test') > 3000 --
```
`appSAFE` uses input handling and treats inputs as a value to test against the database rather than treating it as a regular full string

#### Safe Corrected Code

```
query = """
        SELECT title, date, location
        FROM events
        WHERE title LIKE ?
    """

search_pattern = f"%{search}%"

try:
    events = connection.execute(query, (search_pattern,)).fetchall()
except sqlite3.Error:
    events = []
```
