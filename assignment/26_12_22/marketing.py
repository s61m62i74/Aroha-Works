'''NOTE: : all expense are in INR and per month basic
SM expense is Rs 125000
RD expense is Rs 80000
GA expense is Rs 75500

Net Sales done is Rs 355000
Total cost of goods sold is Rs 257500

find the following: -
a) Gross Margin
    b) what is total operating expense
    c) what is the income from operation
    d) calc the net income4)
    READ THIS....first ....

    a) Gross Margin
    ....................
    The left over amount after cost of goods sold are taken away from net sales.

    Gross Margin=Net Sales - Cost of Goods Sold

    b) Operating Expenses
    .......................
    The sum of expenses paid for developing and selling the product or service.

    Operating Expenses=Sales & Marketing + Research & Development + General & Administrative


    c) Income From Operations
    .......................
    Net profit from the product or services sold.

    Income From Operations=Gross Margin - Operating Expenses


    d) Net Income
    ....................
    Net income is all income minus total expenses and costs.

    Net Income=Income From Operations + Interest Income - Income Taxes


    In summary, the above accounting formulas are all a person will need to
    generate the two main financial statements. However, to fully explore the financial health of
    person or business knowledge of accounting ratios are required.

    NOTE the abbreviation used here:
    Sales & Marketing(SM)
    Research & Development(RD)
    General Adm(GA)'''

net_sale = int(input("Please enter your net sale: "))
cost_of_good_sold = int(input("Please enter your net sale: "))
interest_income = int(input("Please enter your income interest: "))
income_tax = float(input("Please enter your income tax: "))

sales_marketing = 125000
research_dev = 80000
general_adm = 75500

gross_margin = net_sale - cost_of_good_sold
operating_expense = sales_marketing + research_dev + cost_of_good_sold
income_from_operations = gross_margin - operating_expense
net_income = income_from_operations + interest_income - income_tax

print("Gross Margin: ", gross_margin)
print("Operating expense: ", operating_expense)
print("Income from operations: ", income_from_operations)
print("Net Income: ", net_income)
