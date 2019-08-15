from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_number', models.CharField(max_length=5, verbose_name='출석확인번호')),
                ('title', models.CharField(max_length=30, verbose_name='출석 제목')),
                ('init_datetime', models.DateTimeField(verbose_name='출석가능 시작시간')),
                ('gather_datetime', models.DateTimeField(verbose_name='모임 날짜와 시간')),
                ('expired_datetime', models.DateTimeField(verbose_name='출석가능 만료시간')),
                ('attend_status', models.CharField(choices=[('출석 시작 전', '출석 시작 전'), ('정상 출석 가능', '정상 출석 가능'), ('지각 출석 가능', '지각 출석 가능'), ('출석 시간 만료', '출석 시간 만료')], default='출석불가', max_length=15)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.Group')),
            ],
        ),
        migrations.CreateModel(
            name='AttendConfirm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attend_user', models.CharField(max_length=20, verbose_name='출석 닉네임')),
                ('arrive_time', models.DateTimeField(null=True, verbose_name='도착 시간')),
                ('sub_time', models.IntegerField(null=True, verbose_name='시간 차이')),
                ('attend_check', models.CharField(choices=[('지각', '지각'), ('출석', '출석'), ('결석', '결석')], default='결석', max_length=20)),
                ('attendconfirm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Attend')),
            ],
        ),
    ]
