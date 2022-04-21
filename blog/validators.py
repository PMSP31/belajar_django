from django.forms import ValidationError

def validate_title(value):
    title_input = value
    
    if title_input == 'Bodoh':
        raise ValidationError("Judul Anda Telah Melanggar Peraturan!")