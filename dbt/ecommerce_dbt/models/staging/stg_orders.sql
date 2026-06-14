select
    order_id,
    customer_id,
    product_id,
    quantity,
    amount,
    order_date,
    silver_processed_timestamp
from {{ source('silver', 'orders') }}