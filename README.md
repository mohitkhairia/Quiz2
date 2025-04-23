# Employee Dashboard

## Setup

1. Clone repo  
2. `python3 -m venv .venv && source .venv/bin/activate`  
3. `pip install -r requirements.txt`  
4. Configure `config/settings.py` DATABASES  
5. `python manage.py migrate`  
6. `python manage.py seed_data`  

## Running

```bash
python manage.py runserver