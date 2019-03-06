select count(1),count(if(order_time < date_add(now(),interval -30 minute),1,null)) from tom_orders where order_status = '0'
and deleted = '0' and order_time > curdate();monitor;mysql#
