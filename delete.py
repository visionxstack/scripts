from django.contrib.auth import get_user_model
from weblate_web.payments.models import Payment, Customer

User = get_user_model()

# Remove previous test data
Payment.objects.filter(description="IDOR test payment").delete()
Customer.objects.filter(email="victim@test.local").delete()
User.objects.filter(username="idor_test_user").delete()

# Create fresh test user
user = User.objects.create_user(
    username="idor_test_user",
    email="idor@test.local",
    password="password123"
)

# Create fresh customer
customer = Customer.objects.create(
    email="victim@test.local",
    user_id=user.pk,
    origin="http://127.0.0.1:8000"
)

customer.users.add(user)

# Create payment
payment = Payment.objects.create(
    customer=customer,
    amount=100,
    description="IDOR test payment",
    backend="pay"
)

print("Payment UUID:", payment.pk)
print("Payment URL:", payment.get_absolute_url())
