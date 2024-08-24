from django.contrib.auth.models import  BaseUserManager

class UserManager(BaseUserManager):
    """User Model Manager class."""

    def create_user(self, email, password=None, **kwargs):
        if email:
            email = self.normalize_email(email=email)
        else:
            raise ValueError("Email cannot be empty.")

        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is False:
            raise ValueError("is_staff must be True for superuser")

        if kwargs.get("is_superuser") is False:
            raise ValueError("is_superuser must be True for superuser")

        superuser = self.create_user(email, password, **kwargs)
        return superuser