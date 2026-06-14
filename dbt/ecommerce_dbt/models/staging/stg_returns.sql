select
    return_id,
    order_id,
    return_amount,
    return_date,
    silver_processed_timestamp
from {{ source('silver', 'returns') }}