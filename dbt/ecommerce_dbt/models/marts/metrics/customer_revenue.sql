select
    customer_id,
    count(order_id) as total_orders,
    sum(net_sales) as total_revenue,
    avg(net_sales) as average_revenue_per_order,
    {{ customer_tier('SUM(net_sales)') }} as customer_tier
from {{ ref('fact_sales') }}
group by customer_id