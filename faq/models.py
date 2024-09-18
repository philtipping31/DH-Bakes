from django.db import models


class FAQCategory(models.Model):
    """
    A model representing categories for grouping FAQs.
    """
    name = models.CharField(max_length=255, unique=True,
                            null=False, blank=False)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "FAQ Category"
        verbose_name_plural = "FAQ Categories"

    def __str__(self):
        return self.name


class FAQ(models.Model):
    """
    A model representing frequently asked questions.
    """
    question = models.CharField(max_length=500, null=False, blank=False)
    answer = models.TextField(null=False, blank=False)
    category = models.ForeignKey(FAQCategory, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 help_text="The category this FAQ belongs to.")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True,
                                    help_text="Check this box to make"
                                              "the FAQ visible.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question
