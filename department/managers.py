from django.db import models


class PropertyQuerySet(models.QuerySet):
    """

    """

    def item_by_user(self, user_pk):
        """

        @return:
        """
        return self.filter(pk=user_pk)

    def favorite(self, user):
        """

        @return:
        """
        return self.filter(category__in=user.category_set.all())


class PropertyManager(models.Manager):
    """

    """
    use_in_migrations = True

    def get_queryset(self):
        """

        @return:
        """
        return PropertyQuerySet(self.model, using=self._db)

    def item_by_user(self, user_pk):
        """

        @return:
        """
        return self.get_queryset().item_by_user(user_pk)

    def favorite(self, user):
        """

        @return:
        """
        return self.get_queryset().favorite(user)
