select
    product_id,
    product_name,
    category,
    unit_price,
    silver_processed_timestamp
from {{ source('silver', 'products') }}