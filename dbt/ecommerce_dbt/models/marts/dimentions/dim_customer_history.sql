select
    customer_id,
    city,
    state,
    dbt_valid_from,
    dbt_valid_to
from {{ ref('customer_snapshot') }}