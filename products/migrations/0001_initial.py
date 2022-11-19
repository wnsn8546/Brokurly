# Generated by Django 3.2.13 on 2022-11-19 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('unit', models.CharField(max_length=64)),
                ('weight', models.CharField(max_length=64)),
                ('produt_thum_img', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('produt_detail_img', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('produt_desc_img', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('description', models.TextField(blank=True)),
                ('stock', models.IntegerField()),
                ('sales_rate', models.PositiveIntegerField()),
                ('ship_type', models.CharField(choices=[('샛별배송', '샛별배송'), ('일반택배', '일반택배')], max_length=10)),
                ('allergy', multiselectfield.db.fields.MultiSelectField(choices=[('호두', '호두'), ('대두', '대두'), ('메밀', '메밀'), ('오징어', '오징어'), ('우유', '우유'), ('해당없음', '해당없음'), ('조개류', '조개류'), ('돼지고기', '돼지고기'), ('게', '게'), ('쇠고기', '쇠고기'), ('아황산류', '아황산류'), ('고등어', '고등어'), ('땅콩', '땅콩'), ('토마토', '토마토'), ('새우', '새우'), ('난류', '난류'), ('닭고기', '닭고기'), ('밀', '밀'), ('복숭아', '복숭아')], max_length=67)),
                ('is_crawl', models.BooleanField(default=False)),
                ('crawl_produt_thum_img', models.TextField(blank=True)),
                ('crawl_produt_detail_img', models.TextField(blank=True)),
                ('crawl_produt_desc_img', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '상품',
                'verbose_name_plural': '상품',
                'db_table': '상품',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('products', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='wish_product', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
