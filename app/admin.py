from django.contrib import admin, messages
from .models import Ticket, Comment
from django.contrib.auth.models import User

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ['user', 'text', 'created_at']
    readonly_fields = ['created_at']
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(is_superuser=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'class_name', 'created_by', 'status', 'created_at']
    list_filter = ['status', 'class_name', 'created_at']
    search_fields = ['title', 'description', 'created_by__username']
    readonly_fields = ['created_by', 'created_at']
    inlines = [CommentInline]
    
    fieldsets = (
        ('Ticket Information', {
            'fields': ('title', 'description', 'class_name', 'created_by', 'created_at')
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )
    
    def changelist_view(self, request, extra_context=None):
        open_tickets = self.model.objects.filter(status='open').count()
        total_tickets = self.model.objects.count()
        resolved_tickets = self.model.objects.filter(status='resolved').count()
        if open_tickets > 0:
            messages.warning(
                request,
                f"There are {open_tickets} unresolved ticket(s)!"
            )
        # Show total tickets and total resolved tickets as info messages
        messages.info(
            request,
            f"Total tickets: {total_tickets} | Total resolved: {resolved_tickets}"
        )
        return super().changelist_view(request, extra_context=extra_context)

    def response_add(self, request, obj, post_url_continue=None):
        messages.success(request, "New ticket generated!")
        return super().response_add(request, obj, post_url_continue=post_url_continue)

admin.site.register(Ticket, TicketAdmin)
