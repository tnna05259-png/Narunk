import os

def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

def lines1():
    print("-" * 60)

def lines2():
    print("=" * 60)

def header():
    print('\t============ ระบบคำนวณตารางผ่อนสินค้า ============')

def inputdata():
    price = float(input('กรอกราคาสินค้า (บาท): '))
    dow_payment = float(input('กรอกเงินดาวน์ (บาท): '))
    principal = price - dow_payment
    return principal

def get_months():
    while True:
        month = int(input('เลือกจำนวนงวดผ่อนชำระ (3, 6 หรือ 12 เดือน): '))
        if month in (3, 6, 12):
            return month
        else:
            print('!! จำนวนเดือนไม่ถูกต้อง กรุณาระบุเฉพาะ 3, 6, 12 เดือนเท่านั้น')

def calculate_loan(p, m):
    if m == 3:
        interest_rate = 0.00
    elif m == 6:
        interest_rate = 0.03
    else:
        interest_rate = 0.06

    interest_amount = p * interest_rate
    total_debt = p + interest_amount
    monthly_pay = total_debt / m

    return interest_rate, interest_amount, total_debt, monthly_pay

def schedule_table(months, monthly_pay, total_debt):
    print(f"{'งวดที่':<14} | {'ยอดชำระ (บาท)':<20} | {'คงเหลือ (บาท)':<20}")
    lines1()

    balance = total_debt

    for mt in range(1, months + 1):
        balance -= monthly_pay

        if mt == months or balance < 0:
            balance = 0.0

        print(f"งวดที่ {mt:<8} | {monthly_pay:>20,.2f} | {balance:>20,.2f}")

# โปรแกรมหลัก
clrscr()
lines2()
header()
lines2()

principal = inputdata()
months = get_months()

interest_rate, interest_amount, total_debt, monthly_pay = calculate_loan(principal, months)

print('\n')
lines2()
print(f"ยอดจัดไฟแนนซ์  : {principal:,.2f} บาท")
print(f"ดอกเบี้ย ({interest_rate * 100:.0f}%) : {interest_amount:,.2f} บาท")
print(f"ยอดผ่อนรวมสุทธิ : {total_debt:,.2f} บาท")
print(f"ยอดผ่อนต่องวด   : {monthly_pay:,.2f} บาท")
lines2()

schedule_table(months, monthly_pay, total_debt)
lines2()
