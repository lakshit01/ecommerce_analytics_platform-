{{ config(
    materialized = 'incremental',
    unique_key = 'order_id',
    incremental_strategy = 'merge'
)}}

select
    *
from {{ref('int_orders_details')}}

{% if is_incremental() %}

where order_date >= dateadd(day, -7, (select max(order_date) from {{ this }}))

{% endif %}