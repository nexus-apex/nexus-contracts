from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Contract, Party, Amendment
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusContracts with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexuscontracts.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Contract.objects.count() == 0:
            for i in range(10):
                Contract.objects.create(
                    title=f"Sample Contract {i+1}",
                    party=f"Sample {i+1}",
                    contract_type=random.choice(["service", "employment", "nda", "lease", "vendor"]),
                    value=round(random.uniform(1000, 50000), 2),
                    start_date=date.today() - timedelta(days=random.randint(0, 90)),
                    end_date=date.today() - timedelta(days=random.randint(0, 90)),
                    status=random.choice(["draft", "active", "expired", "terminated"]),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Contract records created'))

        if Party.objects.count() == 0:
            for i in range(10):
                Party.objects.create(
                    name=f"Sample Party {i+1}",
                    contact_person=f"Sample {i+1}",
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    party_type=random.choice(["client", "vendor", "partner", "employee"]),
                    active_contracts=random.randint(1, 100),
                )
            self.stdout.write(self.style.SUCCESS('10 Party records created'))

        if Amendment.objects.count() == 0:
            for i in range(10):
                Amendment.objects.create(
                    contract_title=f"Sample Amendment {i+1}",
                    amendment_type=random.choice(["extension", "modification", "termination"]),
                    effective_date=date.today() - timedelta(days=random.randint(0, 90)),
                    description=f"Sample description for record {i+1}",
                    status=random.choice(["proposed", "approved", "applied"]),
                )
            self.stdout.write(self.style.SUCCESS('10 Amendment records created'))
