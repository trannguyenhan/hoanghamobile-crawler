### Install

```bash
pip3 install kafka-python
```

### Run

start `kafka` and create topic `hoangha1`

run spider with command: 

```bash
scrapy crawl smartphone
```

### Crontab

Run command and choose scheduler:

```bash
crontab -e
```

Add last line to command: 

```
0 0 * * * python3 path-to-project/main.py
```
