from django.db import models

# Create your models here.
class ContactModel(models.Model):
    GENDER = (
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan')
    )
    nama_lengkap = models.CharField(max_length=50)
    jenis_kelamin = models.CharField(max_length=1, choices=GENDER)
    # tanggal_lahir = models.DateField()
    email = models.EmailField()
    sign_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.nama_lengkap}"
