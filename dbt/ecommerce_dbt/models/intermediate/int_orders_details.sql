select
    o.order_id,
    o.customer_id,
    o.product_id,
    o.quantity,
    o.amount,
    o.order_date,
    c.customer_first_name,
    c.customer_last_name,
    c.city,
    c.state,
    p.product_name,
    p.category,
    p.unit_price
from {{ ref('stg_orders')}} o
left join {{ ref('stg_customers') }} c
    on o.customer_id = c.customer_id
left join {{ ref('stg_products') }} p
    on o.product_id = p.product_id