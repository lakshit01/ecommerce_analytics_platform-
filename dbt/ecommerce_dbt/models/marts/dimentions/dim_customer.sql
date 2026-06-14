select
    {{ dbt_utils.generate_surrogate_key(['customer_id'])}} as customer_sk,
    customer_id,
    customer_first_name,
    customer_last_name,
    email,
    city,
    state,
    signup_date
from {{ ref('stg_customers') }}