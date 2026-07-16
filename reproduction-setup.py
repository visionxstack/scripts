from django.contrib.auth import get_user_model
from weblate_web.payments.models import Payment, Customer

User = get_user_model()

user = User.objects.create_user(
    username="evidence_user",
    email="evidence@test.local",
    password="TestPassword123!"
)

customer = Customer.objects.create(
    email="evidence@test.local",
    user_id=user.pk,
    origin="http://127.0.0.1:8000",
)

customer.users.add(user)

payment = Payment.objects.create(
    customer=customer,
    amount=100,
    description="IDOR evidence payment",
    backend="pay",
)

print("Payment UUID:", payment.pk)
print("Payment URL:", payment.get_absolute_url())
