{% macro customer_tier(total_sales) %}

CASE

    WHEN coalesce({{ total_sales }}, 0) >= 100000
        THEN 'Platinum'

    WHEN coalesce({{ total_sales }}, 0) >= 50000
        THEN 'Gold'

    WHEN coalesce({{ total_sales }}, 0) >= 10000
        THEN 'Silver'

    ELSE 'Bronze'

END

{% endmacro %}