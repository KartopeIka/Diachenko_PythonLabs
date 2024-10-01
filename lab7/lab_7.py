def print_workers(workers):
    to_print = ""
    for worker, data in workers.items():
        to_print += f"{worker}: salary {data['salary']} grn/day; sex {data['sex']}\n"
    print(to_print)

def delete_worker(workers):
    key = input("Input name of a worker you want to delete: ")
    if key in workers:
        del workers[key]
        print(f"Data about {key} was deleted")
        print_workers(workers)
    else:
        print(f"Did not found worker '{key}'")

def add_worker(workers):
    key = input("Input name of a worker you want to add: ")
    if key in workers:
        print(f"Name '{key}' is already exists")
    else:
        workers[key] = {"salary": input("Input salary: "), "sex": input("Input sex: ")}
        print(f"Added worker {key}")
        print_workers(workers)

def sort_workers(workers):
    workers = {k: workers[k] for k in sorted(workers)}
    print("Sorted data:")
    print_workers(workers)

def find_max_salary_worker(workers):
    max_salary = workers.get(next(iter(workers))).get('salary')
    max_worker = next(iter(workers))
    for worker, data in workers.items():
        if data['salary'] > max_salary:
            max_salary = data['salary']
            max_worker = worker
    print(f"{max_worker} has the highest salary: {max_salary} grn/day")

def find_min_salary_by_sex(workers, sex):
    min_worker = ''
    for worker, data in workers.items():
        if data['sex'] == sex:
            min_salary = data['salary']
            min_worker = worker
        if min_worker:
            break
    if min_worker:
        for worker, data in workers.items():
            if data['sex'] == sex:
                if data['salary'] < min_salary:
                    min_salary = data['salary']
                    min_worker = worker
        print(f"{sex} {min_worker} has the lowest salary: {min_salary} grn/day")
    else: print(f"There is no workers with sex '{sex}'")


coworkers = {'James':{'salary': 1000, 'sex': 'M'},
             'Stacy':{'salary':2000,'sex': 'F'},
             'Kitty':{'salary':1150,'sex': 'F'},
             'Bob':{'salary':2999,'sex': 'M'},
             'Garry':{'salary':800,'sex': 'M'},
             'Stan':{'salary':3500,'sex': 'M'},
             'Linda':{'salary':1790,'sex': 'F'},
             'Mia':{'salary':2400,'sex': 'F'},
             'larry':{'salary':1670,'sex': 'M'},
             'Greg':{'salary':999,'sex': 'M'},
             'Anna':{'salary':1234,'sex': 'F'}}

while True:
    print("Available actions:\n"
          "1: Print information about coworkers\n"
          "2: Add new coworker\n"
          "3: Delete coworker\n"
          "4: Sort coworkers by name\n"
          "5: Find coworker with the highest salary\n"
          "6: Find male and female coworkers with the lowest salary\n"
          "0: Exit\n")
    user_wish = input()
    match user_wish:
        case '0':
            break
        case '1':
            print_workers(coworkers)
        case '2':
            add_worker(coworkers)
        case '3':
            delete_worker(coworkers)
        case '4':
            sort_workers(coworkers)
        case '5':
            find_max_salary_worker(coworkers)
        case '6':
            find_min_salary_by_sex(coworkers, 'M')
            find_min_salary_by_sex(coworkers, 'F')
        case _:
            print("There is no such a variant. Try again")
    print(" -=- "*5)