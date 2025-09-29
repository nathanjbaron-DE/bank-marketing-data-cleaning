# Bank Marketing Data Pipeline (Python, ETL)

## Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) process using Python and Pandas.
The goal is to clean and transform raw bank marketing data into structured CSV files for client, campaign, and economic information.

## Features
- Extracts raw CSV data (bank_marketing.csv)
- Transforms the dataset by:
  - Cleaning string columns (job, education)
  - Standardizing and converting categorical columns to boolean (credit_default, mortgage, previous_outcome, campaign_outcome)
  - Setting last_contact_date to a consistent timestamp
- Loads clean datasets into separate CSV files:
  - client.csv – client demographic and credit info
  - campaign.csv – campaign interaction details
  - economics.csv – economic indicators for each client

## Tech Stack
- Python (pandas, numpy)
- ETL pipeline design

## Files
- `pipeline.py` – ETL pipeline script
- `bank_marketing.csv` – raw input dataset
- `client.csv` – cleaned client dataset
- `campaign.csv` – cleaned campaign dataset
- `economics.csv` – cleaned economic dataset
- `requirements.txt` – Python dependencies
- `README.md` – Project documentation

## How to Run
#### Go to Documents folder
```cd ~/Documents```

#### Clone repo
```git clone https://github.com/nathanjbaron-DE/bank-marketing-data-cleaning.git```

```cd bank-marketing-data-cleaning```

#### Create virtual environment
```python3 -m venv venv```

#### Activate virtual environment
```source venv/bin/activate```

#### Upgrade pip
```pip install --upgrade pip```

#### Install dependencies
```pip install -r requirements.txt```

#### Run the ETL pipeline (outputs saved in current folder)
python3 pipeline.py

#### Check outputs
ls *.csv
