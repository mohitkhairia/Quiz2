from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Department, Employee, Attendance, Performance
import random
from datetime import date, timedelta

class Command(BaseCommand):
    help = "Seed the database with synthetic employee data"

    def handle(self, *args, **options):
        fake = Faker()
        # 4 Departments
        deps = []
        for name in ['Engineering','HR','Sales','Marketing']:
            d, _ = Department.objects.get_or_create(
                name=name,
                defaults={'location': fake.city(), 'budget': random.uniform(50000,200000)}
            )
            deps.append(d)

        # 5 Employees each
        employees = []
        for _ in range(5):
            dept = random.choice(deps)
            emp = Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                date_joined=fake.date_between(start_date='-2y', end_date='today'),
                department=dept,
                salary=round(random.uniform(30000,120000),2)
            )
            employees.append(emp)

            # Attendance for last 30 days
            for i in range(30):
                day = date.today() - timedelta(days=i)
                Attendance.objects.create(
                    employee=emp,
                    date=day,
                    status=random.choice(['Present','Absent']),
                    hours_worked=round(random.uniform(0,8),2)
                )

            # 3 performance reviews
            for q in ['Q1', 'Q2', 'Q3']:
                Performance.objects.create(
                    employee=emp,
                    review_period=f"{q} {date.today().year}",
                    score=random.randint(1,10),
                    remarks=fake.sentence(nb_words=6)
                )

        self.stdout.write(self.style.SUCCESS("Seeded departments, employees, attendance, performance."))