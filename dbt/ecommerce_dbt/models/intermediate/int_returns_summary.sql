select
    order_id,
    sum(return_amount) as total_return_amount,
    count(*) as total_returns
from {{ ref('stg_returns') }}
group by order_id