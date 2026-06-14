select
    customer_id,
    count(order_id) as total_orders,
    sum(amount) as total_sales,
    avg(amount) as average_order_value,
    {{ customer_tier('SUM(amount)') }} as customer_tier
from {{ ref('stg_orders') }}
group by customer_id