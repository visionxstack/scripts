from django.contrib.auth import get_user_model
from weblate_web.payments.models import Payment, Customer

User = get_user_model()

user, _ = User.objects.get_or_create(
    username="idor_test_user",
    defaults={
        "email": "idor@test.local",
    }
)

customer, _ = Customer.objects.get_or_create(
    email="victim@test.local",
    defaults={
        "user_id": user.pk,
        "origin": "http://127.0.0.1:8000",
    }
)

customer.users.add(user)

payment = Payment.objects.create(
    customer=customer,
    amount=100,
    description="IDOR test payment",
    backend="pay"
)

print("Payment UUID:", payment.pk)
print("Payment URL:", payment.get_absolute_url())
