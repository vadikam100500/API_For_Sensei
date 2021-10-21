# API_For_Sensei
- Simple API on django by TOR of mentor.

## What I used

> - django==2.2.6
> - djangorestframework
> - django_filters
> - requests

## How to install

```sh
$ python3 -m venv 'name of virtual environment'
$ venv 'name of virtual environment'/Scripts(or bin for linux)/activate
$ pip install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

## Database

```sh
$ python3 manage.py database <Your url adress>
```

# Task

Dataset: https://gist.github.com/artrey/8d6a3f2d91cefb5e6343bedbc9ef8c79

Вам необходимо разработать API сервис для выдачи информации из датасета выше. Клиент должен иметь возможность:

1. Получать только запрошенные колонки
2. Фильтровать данные по одной или нескольким колонкам: дате (from/to), магазинам, странам
3. Группировать данные по одной или нескольким колонкам: датам, магазинам, странам
4. Сортировать по любой из колонок

Если клиент не указывает, какие колонки необходимо отобразить, то требуется отобразить все колонки.

Не забываем про пагинацию.

---

Примеры запросов (ваши запросы могут отличаться, главное, чтобы они выполняли поставленную задачу):

1. Показать сырые данные вида `Date - Visitors - Earnings`
```bash
api/v1/metrics/?show=date&show=visitors&show=earnings
```
2. Показать сырые данные вида `Date - Country - Visitors - Earnings` за промежуток с 2021-03-20 по 2021-06-01
```bash
api/v1/metrics/?show=date&show=country&show=visitors&show=earnings&date_from=2021-03-20&date_to=2021-06-01
```
3. Показать сгруппированные данные по странам, при этом отобразить `Earnings` и упорядочить по убыванию по `Earnings`
```bash
api/v1/metrics/?group=country&show=earnings&o=-earnings
```
4. Показать сгруппированные данные по магазинам и странам и при этом отобразить `Visitors`
```bash
api/v1/metrics/?group=country&group=shop&show=visitors
```
