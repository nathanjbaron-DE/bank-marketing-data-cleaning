# pipeline.py
import pandas as pd
import numpy as np

def main():
    # -----------------------------
    # Extract
    # -----------------------------
    df = pd.read_csv("bank_marketing.csv")
    
    # -----------------------------
    # Transform
    # -----------------------------
    # Clean job and education columns
    df['job'] = df['job'].str.replace(".", "_")
    df['education'] = df['education'].str.replace(".", "_").replace("unknown", np.NaN)
    
    # Standardize credit_default column
    df.loc[df['credit_default'] == 'yes', 'credit_default'] = 1
    df.loc[df['credit_default'].isin(['no', 'unknown']), 'credit_default'] = 0
    df['credit_default'] = df['credit_default'].astype(bool)
    
    # Standardize mortgage column
    df.loc[df['mortgage'] == 'yes', 'mortgage'] = 1
    df.loc[df['mortgage'].isin(['no', 'unknown']), 'mortgage'] = 0
    df['mortgage'] = df['mortgage'].astype(bool)
    
    # Standardize previous_outcome column
    df.loc[df['previous_outcome'] == 'success', 'previous_outcome'] = 1
    df.loc[df['previous_outcome'].isin(['failure', 'nonexistent']), 'previous_outcome'] = 0
    df['previous_outcome'] = df['previous_outcome'].astype(bool)
    
    # Standardize campaign_outcome column
    df.loc[df['campaign_outcome'] == 'yes', 'campaign_outcome'] = 1
    df.loc[df['campaign_outcome'].isin(['no', 'unknown']), 'campaign_outcome'] = 0
    df['campaign_outcome'] = df['campaign_outcome'].astype(bool)
    
    # Set last_contact_date column
    df['last_contact_date'] = pd.to_datetime('2022-07-10')
    
    # -----------------------------
    # Load
    # -----------------------------
    # Client information CSV
    client_columns = ['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']
    df[client_columns].to_csv('client.csv', index=False)
    
    # Campaign information CSV
    campaign_columns = ['client_id', 'number_contacts', 'contact_duration', 
                        'previous_campaign_contacts', 'previous_outcome', 
                        'campaign_outcome', 'last_contact_date']
    df[campaign_columns].to_csv('campaign.csv', index=False)
    
    # Economics information CSV
    economics_columns = ['client_id', 'cons_price_idx', 'euribor_three_months']
    df[economics_columns].to_csv('economics.csv', index=False)
    
    print("ETL pipeline completed successfully. CSV files generated:")
    print(" - client.csv")
    print(" - campaign.csv")
    print(" - economics.csv")

if __name__ == "__main__":
    main()
