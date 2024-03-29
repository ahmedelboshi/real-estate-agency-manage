from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Workflow(models.Model):

    name = models.CharField(_("name"), max_length=50)

    class Meta:
        verbose_name = _("Workflow")
        verbose_name_plural = _("Workflows")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Workflow_detail", kwargs={"pk": self.pk})

class Step(models.Model):
    
    step_type = models.CharField(_("step type"), max_length=50)
    order = models.PositiveIntegerField(_("order"))
    workflow = models.ForeignKey("workflow.Workflow", related_name="steps",verbose_name=_("steps"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Step")
        verbose_name_plural = _("Steps")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Step_detail", kwargs={"pk": self.pk})

class StepAttribute(models.Model):
    title = models.CharField(_("title"), max_length=250)
    step = models.ForeignKey("workflow.Step", verbose_name=_("attributes"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("StepAttribute")
        verbose_name_plural = _("StepAttributes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("StepAttribute_detail", kwargs={"pk": self.pk})
