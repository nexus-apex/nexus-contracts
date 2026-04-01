from django.db import models

class Contract(models.Model):
    title = models.CharField(max_length=255)
    party = models.CharField(max_length=255, blank=True, default="")
    contract_type = models.CharField(max_length=50, choices=[("service", "Service"), ("employment", "Employment"), ("nda", "NDA"), ("lease", "Lease"), ("vendor", "Vendor")], default="service")
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[("draft", "Draft"), ("active", "Active"), ("expired", "Expired"), ("terminated", "Terminated")], default="draft")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Party(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    party_type = models.CharField(max_length=50, choices=[("client", "Client"), ("vendor", "Vendor"), ("partner", "Partner"), ("employee", "Employee")], default="client")
    active_contracts = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Amendment(models.Model):
    contract_title = models.CharField(max_length=255)
    amendment_type = models.CharField(max_length=50, choices=[("extension", "Extension"), ("modification", "Modification"), ("termination", "Termination")], default="extension")
    effective_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, default="")
    status = models.CharField(max_length=50, choices=[("proposed", "Proposed"), ("approved", "Approved"), ("applied", "Applied")], default="proposed")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.contract_title
