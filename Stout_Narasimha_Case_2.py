import pandas as pd

df = pd.read_csv("casestudy.csv")
customer_2015 = df[df.year.isin(['2015'])]
customer_2016 = df[df.year.isin(['2016'])]
customer_2017 = df[df.year.isin(['2017'])]
customer_2016_17 = df[df.year.isin(['2016', '2017'])]


new_customer_2016 = customer_2016[~customer_2016.customer_email.isin(customer_2015['customer_email'])]
new_customer_2017_1 = customer_2017[~customer_2017.customer_email.isin(customer_2016['customer_email'])]
new_customer_2017 = new_customer_2017_1[~new_customer_2017_1.customer_email.isin(customer_2015['customer_email'])]
print("New customers 2015 net revenue: ", customer_2015['net_revenue'].sum())
print("New customers 2016 net revenue: ", new_customer_2016['net_revenue'].sum())
print("New customers 2017 net revenue: ", new_customer_2017['net_revenue'].sum())

existing_15_16 = customer_2015[customer_2015.customer_email.isin(customer_2016['customer_email'])]['customer_email']
existing_15_17 = customer_2015[customer_2015.customer_email.isin(customer_2017['customer_email'])]['customer_email']
existing_16_17 = customer_2016[customer_2016.customer_email.isin(customer_2017['customer_email'])]['customer_email']

cg1516 = customer_2016[customer_2016.customer_email.isin(existing_15_16)]['net_revenue'].sum() - customer_2015[customer_2015.customer_email.isin(existing_15_16)]['net_revenue'].sum()
cg1517 = customer_2017[customer_2017.customer_email.isin(existing_15_17)]['net_revenue'].sum() - customer_2015[customer_2015.customer_email.isin(existing_15_16)]['net_revenue'].sum()
cg1617 = customer_2017[customer_2017.customer_email.isin(existing_16_17)]['net_revenue'].sum() - customer_2016[customer_2016.customer_email.isin(existing_16_17)]['net_revenue'].sum()
print("Existing customer growth 2015-2016: ", cg1516)
print("Existing customer growth 2015-2017: ", cg1517)
print("Existing customer growth 2016-2017: ", cg1617)

leaving_2015 = customer_2015[~customer_2015.customer_email.isin(customer_2016_17['customer_email'])]['net_revenue'].sum()
print("Revenue lost from 2015 attrtion: ", leaving_2015)
leaving_2016 = customer_2016[~customer_2016.customer_email.isin(customer_2017['customer_email'])]['net_revenue'].sum()
print("Revenue lost from 2016 attrition: ", leaving_2016)

existing_2016 = customer_2016[customer_2016.customer_email.isin(customer_2015['customer_email'])]['net_revenue'].sum()
existing_2015_17 = customer_2017[customer_2017.customer_email.isin(customer_2015['customer_email'])]['net_revenue'].sum()
existing_2016_17 = customer_2017[customer_2017.customer_email.isin(new_customer_2016['customer_email'])]['net_revenue'].sum()
print("Existing customer revenue current year 2016: ", existing_2016)
print("Existing customer revenue current year 2017: ", existing_2015_17 + existing_2016_17)

prior_2015 = customer_2015[customer_2015.customer_email.isin(customer_2016['customer_email'])]['net_revenue'].sum()
prior_2015_17 = customer_2015[customer_2015.customer_email.isin(new_customer_2017_1['customer_email'])]['net_revenue'].sum()
prior_2016 = customer_2016[customer_2016.customer_email.isin(customer_2017['customer_email'])]['net_revenue'].sum()
print("Existing customer revenue prior year 2017: ", prior_2015_17 + prior_2016)
print("Existing customer revenue current year 2016: ", prior_2015)

lost_2015_1 = customer_2015[~customer_2015.customer_email.isin(customer_2016['customer_email'])]
lost_2015 = lost_2015_1[~lost_2015_1.customer_email.isin(customer_2017['customer_email'])]
lost_2016 = customer_2016[~customer_2016.customer_email.isin(customer_2017['customer_email'])]

print("New customers in 2015: ", len(customer_2015.index))
print("New customers in 2016: ", len(new_customer_2016.index))
print("New customers in 2017: ", len(new_customer_2017.index))

print("Lost customers from 2015: ", len(lost_2015.index))
print("Lost customers from 2016: ", len(lost_2016.index))
