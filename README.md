<div align="center">
  <h1>TelegramBot KinoPoisk</h1>
  <p>TelegramBot взаимодействует с <a href="https://kinopoiskapiunofficial.tech/">API КиноПоиска</a></p>
</div>

## Навигация

* [Создание бота](#создание-бота)
  * [Получение токена KinopoiskAPI](#получение-токена-kinopoiskapi)
  * [Получение токена Telegram в BotFather](#получение-токена-telegram-в-botfather)
  * [Структура Бота](#структура-бота)
* [Запуск БОТА](#запуск-бота)
  * [Команда для запуска бота](#команда-для-запуска-бота)
  * [Работа БОТА](#работа-бота)
  * [Поиск фильма](#поиск-фильма)
  * [Возвращаемые параметры](#возвращаемые-параметры)
  
#Создание бота 
### Получение токена KinopoiskAPI
Для получение информации о фильмах воспользуемся неофициальным API кинопоиска.
В начале зарегистрируемся на сайте
<a href="https://kinopoiskapiunofficial.tech/signup">kinopoiskapiunofficial.tech</a>.
После регистрации в настройках профиля станет доступен token для доступа на API.

### Получение токена Telegram в BotFather
Далее нужно инициализировать бота в телеграмме. Для этого перейдем по ссылке
 <a href="https://t.me/BotFather">BotFather</a>. Далее в диалоге с ботом нажмем кнопку запустить.
Переходим к созданию нового бота, отправляем команду «/newbot». В ответ на данную команду BotFather спросит нас о имени нашего бота Telegram.
Указываем любое произвольное имя. Я дал имя cinema_sirius. После требуется придумать уникальный идентификатор, для продолжения регистрации Telegram бота. 
Мой <a href="https://t.me/DeadlyFeBot">DeadlyFeBot</a>. После этого BotFather пришлет уникальный токен бота и ссылку на документацию. Сохраним данный token.

### Структура Бота
Бот состоит из трех файлов. Файл .env содержит вышеупомянутые токены кинопоиска и телеграмма. Файл kinopoisk_api.py реализует 
асинхронные запросы на неофициальный API и получение информации о фильме. Файл bot.py реализует запросы на телеграмм.
Бот запущен на сервере AWS. 

## Запуск БОТА
Ввод команды в терминале.

### Команда для запуска бота
$ python bot.py
или же 
$ BOT_TOKEN=<your own token> python bot.py
для просмотра работы бота на локальной машине

### Работа БОТА
Бот обрабатывает две команды /start и /help.
Переходим по ссылке <a href="https://t.me/DeadlyFeBot">DeadlyFeBot</a> отправляем команду /start.
Следующий шаг отправляем боту название фильма.

### Поиск фильма
Поиск осуществляется по названию как на русском, так и на английском языках.
Если в процессе поиска по отправленному ему названию бот находит 3 и более совпадений, бот
присылает только первые три фильма.
В том случае если бот ничего не находит, отвечает следующей фразой.

> По вашему запросу ничего не смог найти, пожалуйста введите корректное название фильма.

### Поиск фильма по ключевому слову

> Рэмбо


### Возвращаемые параметры
> Постер к фильму
>
> Название: Рэмбо: Первая кровь
>
> Год производства: 1982
> 
> Жанр: боевик, приключения
> 
> Страна: США
> 
> Время просмотра: 1:33
> 
> Рейтинг: 7.7

> Ссылка на сайт КиноПоиска

<img align="center" src="https://disk.yandex.ru/i/3X1mXgSXUP4kzw" alt="Сообщение">