import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits
# print(all_visitors)
paying_visitors = noshmishmosh.purchasing_customers 
# print(paying_visitors)

total_visitor_count = len(all_visitors)
# print(total_visitor_count)
paying_visitor_count = len(paying_visitors)
# print(paying_visitor_count)

baseline_percent = (paying_visitor_count / total_visitor_count) * 100.0
# print(baseline_percent)

payment_history = noshmishmosh.money_spent
# print(payment_history)
average_payment = np.mean(payment_history)
# print(average_payment)
new_customers_needed = np.ceil(1240 / average_payment)
# print(new_customers_needed)
percentage_point_increase = (new_customers_needed / total_visitor_count) * 100.0
# print(percentage_point_increase)

lift = (percentage_point_increase / baseline_percent) * 100
# print(lift)

ab_sample_size = 494
print(ab_sample_size)
