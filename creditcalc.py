import argparse
import math
parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
args = parser.parse_args()

def check_arg_amount(x):
    count = [x.type, x.payment, x.principal, x.periods, x.interest]
    count = [n for n in count if n is not None]
    if len(count) < 4:
        return True
    else:
        return False

def check_arg_negatives(x):
    if x.payment != None and float(x.payment) < 0:
        return True
    elif x.principal != None and float(x.principal) < 0:
        return True
    elif x.periods != None and float(x.periods) < 0:
        return True
    elif x.interest != None and float(x.interest) < 0:
        return True
    else:
        return False

if args.type != 'diff' and args.type != 'annuity':
    print('Incorrect parameters.')
elif args.type == 'diff' and args.payment != None:
    print('Incorrect parameters.')
elif args.interest == None:
    print('Incorrect parameters.')
elif check_arg_amount(args):
    print('Incorrect parameters.')
elif check_arg_negatives(args):
    print('Incorrect parameters.')
elif args.type == 'diff':  # Differentiated payment amount
    princip = float(args.principal)
    periods = float(args.periods)
    interest = float(args.interest) / (12 * 100)
    overpayment = 0
    for i in range(int(args.periods)):
        payment = math.ceil(princip / periods + interest * (princip - (princip * i) / periods))
        overpayment += payment
        output_month = i + 1
        print(f'Month {output_month}: payment is {payment}')
    overpayment -= princip
    output_overpayment = math.ceil(overpayment)
    print(f'\nOverpayment = {output_overpayment}')
elif args.type == 'annuity':  # Annuity payment scheme
    if args.payment == None:  # Monthly payment amount
        princip = float(args.principal)
        periods = float(args.periods)
        interest = float(args.interest) / (12 * 100)
        payment = math.ceil(princip * ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)))
        overpayment = math.ceil(payment * periods - princip)
        print(f'Your annuity payment = {payment}!')
        print(f'Overpayment = {overpayment}')
    elif args.principal == None:  # Principal
        payment = float(args.payment)
        periods = float(args.periods)
        interest = float(args.interest) / (12 * 100)
        princip = int(payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)))
        overpayment = math.ceil(payment * periods - princip)
        print(f'Your loan principal = {princip}!')
        print(f'Overpayment = {overpayment}')
    elif args.periods == None:  # Number of monthly payments
        princip = float(args.principal)
        payment = float(args.payment)
        interest = float(args.interest) / (12 * 100)
        months = math.ceil(math.log(payment / (payment - interest * princip), 1 + interest))
        periods = months
        years = months // 12
        months %= 12
        if years == 0:
            if months == 1:
                print(f'It will take 1 month to repay this loan!')
            else:
                print(f'It will take {months} months to repay this loan!')
        elif years == 1:
            if months == 0:
                print(f'It will take 1 year to repay this loan!')
            elif months == 1:
                print(f'It will take 1 year and 1 month to repay this loan!')
            else:
                print(f'It will take 1 year and {months} months to repay this loan!')
        else:
            if months == 0:
                print(f'It will take {years} years to repay this loan!')
            elif months == 1:
                print(f'It will take {years} years and 1 month to repay this loan!')
            else:
                print(f'It will take {years} years and {months} months to repay this loan!')
        overpayment = math.ceil(payment * periods - princip)
        print(f'Overpayment = {overpayment}')