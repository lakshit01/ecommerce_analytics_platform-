select
    customer_id,
    first_name as customer_first_name,
    last_name as customer_last_name,
    email,
    city,
    state,
    signup_date,
    silver_processed_timestamp
from {{ source('silver', 'customers') }}