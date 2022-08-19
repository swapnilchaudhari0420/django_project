from django.db import models

# Create your models here.

class register_table(models.Model):
    username = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return self.username



class appointment_table(models.Model):
    destination = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    beardo = (('nun', "nun"),
              ('Classic', "Classic"),
              ('Anchar', "Anchar"),
              ('ducktail', "ducktail"),
              ('Verdi', "Verdi"),
              ('chin curtain', "chin curtain"),
              ('soul patch', "soul patch"),
              ('french fork', "french fork"),
              ('sparrow', "sparrow"),
              ('full grownth', "full grownth"),
              ('full goatee', "full goatee"))
    beard = models.CharField(max_length=30, choices=beardo, default='nun')

    hair_style = (('nun', "nun"),
                  ('Deco Wing Bun Cuff', "Deco Wing Bun Cuff"),
                  ('Waterfall Braid', "Waterfall Braid"),
                  ('Crown Braid', "Crown Braid"),
                  ('hairband look', "hairband look"),
                  ('side ponytail', "side ponytail"),
                  ('Braided Bun', "Braided Bun"),
                  ('Ladder Braid', "Ladder Braid"),
                  ('half up half down', "half up half down"),
                  ('high pouf ponytail', "high pouf ponytail"),
                  ('curly', "curly"))
    hairstyle = models.CharField(max_length=30, choices=hair_style, default='nun')

    hair_cut = (('nun', "nun"),
                ('Wispy', "Wispy"),
                ('A line cut', "A line cut"),
                ('Feather cut', "Feather cut"),
                ('bob cut', "bob cut"),
                ('pixie cut', "pixie cut"),
                ('Bangs With feather cut', "Bangs With feather cut"),
                ('Bangs with straight', "Bangs with straight"),
                ('diana cut', "diana cut"),
                ('V cut', "V cut"),
                ('U cut', "U cut"))
    haircut = models.CharField(max_length=30, choices=hair_cut, default='nun')

    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    objects = models.Manager()
    def __str__(self):
        return self.destination

