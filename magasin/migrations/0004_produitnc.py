# Generated by Django 4.1.7 on 2023-02-28 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0003_categorie_fournisseur_produit_fournisseur_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduitNC',
            fields=[
                ('produit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='magasin.produit')),
                ('Duree_garantie', models.CharField(max_length=100)),
            ],
            bases=('magasin.produit',),
        ),
    ]
