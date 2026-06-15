{{ config(
    materialized='incremental',
    unique_key='order_id',
    incremental_strategy='merge'
)}}

SELECT

    o.order_id,
    c.customer_sk,
    p.product_sk,

    o.customer_id,
    o.product_id,

    o.order_date,
    o.quantity,
    o.amount,

    COALESCE(
        r.total_return_amount,
        0
    ) AS return_amount,

    o.amount -
    COALESCE(
        r.total_return_amount,
        0
    ) AS net_sales

FROM {{ ref('int_orders_details') }} o

LEFT JOIN {{ ref('dim_customer') }} c
ON o.customer_id = c.customer_id

LEFT JOIN {{ ref('dim_product') }} p
ON o.product_id = p.product_id

LEFT JOIN {{ ref('int_returns_summary') }} r
ON o.order_id = r.order_id

{% if is_incremental() %}

WHERE o.order_date >= (
    SELECT date_sub(max(order_date), 7)
    FROM {{ this }}
)

{% endif %}