from django.db import models

# Create your models here.
class TeleSettings(models.Model):
    tg_token=models.CharField(max_length=200,verbose_name="Telegram Token")
    tg_chat=models.CharField(max_length=200,verbose_name="Chat ID")
    tg_message=models.TextField(verbose_name="Message Text")



    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"
