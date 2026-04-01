from django.contrib import admin
from .models import Contract, Party, Amendment

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ["title", "party", "contract_type", "value", "start_date", "created_at"]
    list_filter = ["contract_type", "status"]
    search_fields = ["title", "party"]

@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ["name", "contact_person", "email", "phone", "party_type", "created_at"]
    list_filter = ["party_type"]
    search_fields = ["name", "contact_person", "email"]

@admin.register(Amendment)
class AmendmentAdmin(admin.ModelAdmin):
    list_display = ["contract_title", "amendment_type", "effective_date", "status", "created_at"]
    list_filter = ["amendment_type", "status"]
    search_fields = ["contract_title"]
