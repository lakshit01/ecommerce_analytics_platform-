select
    product_id,
    count(order_id) as total_orders,
    sum(net_sales) as total_revenue,
    sum(return_amount) as total_returns
from {{ ref('fact_sales') }}
group by product_id